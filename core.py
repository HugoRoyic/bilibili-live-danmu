import json
import queue
import brotli
import random
import socket
import struct
import sqlite3
import datetime
import requests
import threading
# from kitchen.text.display import textual_width_fill

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
            "uid"	INTEGER,
            "nickname"	TEXT NOT NULL,
            "text"	TEXT NOT NULL,
            "date"	TEXT,
            "time"	TEXT
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

    def start(self, pipe):
        self.get_room_info()
        self.get_room_conf()
        self.get_db_connect()
        self.get_socket_connect()
        self._thread = threading.Thread(target=self.run, args=(pipe,))
        self._thread.start()

    def run(self, pipe):
        self._running = True
        while self._running:
            for data in self.socket_recv():
                pipe.put(self.handle(*data))

    def handle(self, version, msg_type, data):
        if msg_type == TYPE_SERVER_INFO:
            data = json.loads(data)
            cmd = data.get("cmd")
            if cmd == "DANMU_MSG":
                info = data.get("info")
                ts = info[9]["ts"]
                uid, nickname = info[2][:2]
                text = info[1]
                date, time = datetime.datetime.fromtimestamp(ts).isoformat(' ').split()
                d = DanMu(ts=ts, uid=uid, nickname=nickname, text=text, date=date, time=time)
                self.save(d)

                if info[3]:
                    # medal_level, medal, medal_owner = info[3][:3]
                    medal_level, medal = info[3][:2]
                    return {"code": 2,
                            "data": {"medal": f"{medal}{medal_level}",
                                     "nickname": nickname,
                                     "text": text}
                            }
                else:
                    return {"code": 2,
                            "data": {"nickname": nickname,
                                     "text": text}
                            }
            elif cmd == "STOP_LIVE_ROOM_LIST" or "NOTICE_MSG":
                return {"code": 3}
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
            elif cmd == "INTERACT_WORD":
                return {"code": 8}
            else:
                return {"code": 9}
        elif msg_type == TYPE_SERVER_HEARTBEAT:
            return {"code": 1,
                    "data": {"info": f"receive hearbeat {int.from_bytes(data, 'big')}"}
                    }
        elif msg_type == TYPE_SERVER_AUTH:
            return {"code": 0,
                    "data": {"info": "服务器认证通过"}
                    }

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
        # if result["code"] != 0:
        #     {'code': 10031, 'data': [], 'message': '您发送弹幕的频率过快', 'msg': '您发送弹幕的频率过快'}
        #     return(f"发送【{msg}】失败")
        return result

    def save(self, danmu):
        keys = ','.join(danmu.keys())
        values = ','.join(["?"] * len(danmu))
        self._cursor.execute(f"""INSERT OR IGNORE INTO "danmu" ({keys}) VALUES ({values})""", tuple(danmu.values()))
        self._connect.commit()

    def stop(self):
        self._running = False
        self._heartbeat.cancel()
        self.socket_send("", TYPE_CLIENT_HEARTBEAT)
        self._thread.join()
        self._socket.close()
        self._connect.close()


if __name__ == "__main__":
    from config import CONFIG

    c = DanMuJiCore(CONFIG)
    q = queue.Queue()
    c.start(q)

    def handler(pipe):
        while True:
            item = pipe.get()
            if item:
                print(item)
    thread = threading.Thread(target=handler, args=(q,), daemon=True)
    thread.start()
