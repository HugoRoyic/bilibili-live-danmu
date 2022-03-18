import json
# import zlib
import queue
import brotli
import random
import socket
import struct
import sqlite3
import datetime
import requests
import threading
import atexit
from kitchen.text.display import textual_width_fill

from items import DanMu

# 头部各数据字节长度
BYTES_TOTAL = 4
BYTES_HEADER = 2
BYTES_VERSION = 2
BYTES_TYPE = 4
BYTES_CONSTANT = 4
# 头部数据固定值
CONST_HEADER = 16
CONST_CONSTANT = 1
# 协议版本
VERSION_UNZIPPED = 0
VERSION_HEARTBEAT = 1
VERSION_ZIPPED = 3
# 数据包类型
TYPE_CLIENT_HEARTBEAT = 2
TYPE_SERVER_HEARTBEAT = 3
TYPE_SERVER_INFO = 5
TYPE_CLIENT_AUTH = 7
TYPE_SERVER_AUTH = 8


class DanMuJiCore:
    SEND_URL = "https://api.live.bilibili.com/msg/send"
    ROOM_URL = "https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom"
    CONF_URL = "https://api.live.bilibili.com/room/v1/Danmu/getConf"

    def __init__(self, config):
        # config
        self.headers = config.get("headers")
        self.cookies = config.get("cookies")
        self.csrf = config.get("csrf")
        self.roomid = config.get("roomid")
        # room info
        self._uid = None
        self._nickname = None
        self._roomid = None
        self._title = None
        # room conf
        self._url = None
        self._port = None
        self._token = None
        # database connect
        self._cache = set()
        self._connect = None
        self._cursor = None
        # socket connect
        self._socket = None
        # pipeline
        self.pipe = queue.Queue()

    def start(self):
        self.get_room_info()
        self.get_room_conf()
        self.get_db_connect()
        self.get_socket_connect()
        self._getting = True
        self._danmu_enqueue_thread = threading.Thread(target=self.danmu_enqueue, daemon=True)
        self._danmu_enqueue_thread.start()

    def get_room_info(self):
        response = requests.get(self.ROOM_URL, headers=self.headers, params={"room_id": self.roomid})
        data = json.loads(response.content).get("data")
        assert data
        room_info = data["room_info"]
        self._uid = room_info["uid"]
        self._nickname = data["anchor_info"]["base_info"]["uname"]
        self._roomid = room_info["room_id"]
        self._title = room_info["title"]

    def get_room_conf(self):
        response = requests.get(self.CONF_URL, headers=self.headers, params={
                                "room_id": self._roomid, "platform": "pc_link"})
        data = json.loads(response.content).get("data")
        assert data
        self._url = data['host_server_list'][0]['host']
        self._port = data['host_server_list'][0]['port']
        self._token = data['token']

    def get_db_connect(self):
        self._connect = sqlite3.connect(f'history-{self._roomid}.db', check_same_thread=False)
        self._cursor = self._connect.cursor()
        self.create_table()

    def create_table(self):
        self._cursor.execute("""
        CREATE TABLE IF NOT EXISTS "danmu" (
            "ts"	INTEGER,
            "ct"	INTEGER,
            "uid"	INTEGER,
            "nickname"	TEXT NOT NULL,
            "text"	TEXT NOT NULL,
            "date"	TEXT,
            "time"	TEXT,
            PRIMARY KEY("ts", "ct")
        )""")

    def get_socket_connect(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self._url, self._port))
        data = {"uid": 0,
                "roomid": self._roomid,
                "protover": 3,
                "platform": "pc_link",
                "type": 2,
                "key": self._token
                }
        self.socket_send(json.dumps(data, separators=(',', ':')), TYPE_CLIENT_AUTH)
        self.socket_heartbeat()

    def socket_send(self, message, msg_type):
        header = [CONST_HEADER + len(message),
                  CONST_HEADER,
                  VERSION_HEARTBEAT,
                  msg_type,
                  CONST_CONSTANT
                  ]
        message_encoded = struct.pack("!IHHII", *header) + message.encode()
        self._socket.sendall(message_encoded)

    def socket_heartbeat(self):
        self.socket_send("", TYPE_CLIENT_HEARTBEAT)
        self._heartbeat = threading.Timer(30, self.socket_heartbeat)
        self._heartbeat.daemon = True
        self._heartbeat.start()

    @staticmethod
    def unpack_packets(message):
        ptr = 0
        total_length = len(message)
        while ptr < total_length:
            header = message[ptr: ptr + CONST_HEADER]
            length, _, version, msg_type, _ = struct.unpack("!IHHII", header)
            data = message[ptr + CONST_HEADER: ptr+length]
            ptr += length
            yield version, msg_type, data

    def socket_recv(self):
        header = self._socket.recv(CONST_HEADER, socket.MSG_WAITALL)
        length, _, version, msg_type, _ = struct.unpack("!IHHII", header)
        message = self._socket.recv(length-CONST_HEADER, socket.MSG_WAITALL)

        if version == VERSION_ZIPPED:
            for data in DanMuJiCore.unpack_packets(brotli.decompress(message)):
                yield data
        else:
            yield version, msg_type, message

    def danmu_enqueue(self):
        while self._getting:
            for data in self.socket_recv():
                self.pipe.put(self.handle(*data))

    # def danmu_dequeue(self):
    #     if not self.pipe.empty():
    #         return self.pipe.get()

    def handle(self, version, msg_type, data):
        if msg_type == TYPE_SERVER_AUTH:
            return {"code": 0, "msg": "服务器认证通过"}
        elif msg_type == TYPE_SERVER_HEARTBEAT:
            if version == VERSION_HEARTBEAT:
                return {"code": 1, "msg": data}
        elif msg_type == TYPE_SERVER_INFO:
            data = json.loads(data)
            cmd = data.get("cmd")
            if cmd == "DANMU_MSG":
                info = data.get("info")
                text = info[1]
                uid, nickname = info[2][:2]
                medal_level, medal, medal_owner = info[3][:3] or ['  '] * 3
                tsct = info[9]
                ts = tsct["ts"]
                ct = tsct["ct"]
                date_time = datetime.datetime.fromtimestamp(ts).isoformat(' ')
                d = DanMu()
                d["ts"] = ts
                d["ct"] = ct
                d["uid"] = uid
                d["nickname"] = nickname
                d["text"] = text
                d["date"], d["time"] = date_time.split()
                self.save(d)
                return {"code": 3, "msg": "", "meta": [medal, medal_level, medal_owner, d]}
            elif cmd == "STOP_LIVE_ROOM_LIST" or "NOTICE_MSG":
                return
            elif cmd == "ONLINE_RANK_COUNT":
                return {"code": 4}
            elif cmd == "ONLINE_RANK_V2":
                return {"code": 5}
                # print(data["data"]["list"])
            elif cmd.startswith("ONLINE_RANK_TOP"):
                return {"code": 6}
            elif cmd == "WATCHED_CHANGE":
                return {"code": 7}
                # print(data["data"]["text_large"])
            else:
                return {"code": 8}

    def send_danmu(self, msg):
        data = {"bubble": 0,
                "msg": msg,
                "color": 5816798,
                "mode": 1,
                "fontsize": " 25",
                "rnd": random.randint(100000000, 9999999999),
                "roomid": self.roomid,
                "csrf": self.csrf,
                "csrf_token": self.csrf}
        response = requests.post(self.SEND_URL, data=data, cookies={"Cookie": self.cookies})
        result = json.loads(response.content)
        return result
        # if result["code"] != 0:
        #     {'code': 10031, 'data': [], 'message': '您发送弹幕的频率过快', 'msg': '您发送弹幕的频率过快'}
        #     return(f"发送【{msg}】失败")

    def save(self, danmu):
        keys = ','.join(danmu.keys())
        values = ','.join(["?"] * len(danmu))
        self._cursor.execute(f"""INSERT OR IGNORE INTO "danmu" ({keys}) VALUES ({values})""", tuple(danmu.values()))
        self._connect.commit()

    def stop(self):
        self._getting = False
        self._heartbeat.cancel()
        self._connect.close()


if __name__ == "__main__":
    from config import CONFIG

    c = DanMuJiCore(CONFIG)
    c.start()
    c.danmu_dequeue()

    atexit.register(c.stop)
