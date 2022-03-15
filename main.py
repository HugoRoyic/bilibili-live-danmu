import json
# import zlib
import brotli
import random
import socket
import struct
import sqlite3
import requests
import threading
import atexit


from items import DanMu
from config import CONFIG


BYTES_TOTAL = 4
BYTES_HEADER = 2
BYTES_VERSION = 2
BYTES_TYPE = 4
BYTES_CONSTANT = 4

CONST_HEADER = 16
CONST_CONSTANT = 1

VERSION_UNZIPPED = 0
VERSION_HEARTBEAT = 1
VERSION_ZIPPED = 3

TYPE_CLIENT_HEARTBEAT = 2
TYPE_SERVER_HEARTBEAT = 3
TYPE_SERVER_INFO = 5
TYPE_CLIENT_AUTH = 7
TYPE_SERVER_AUTH = 8


class DanMuJi:
    GET_URL = "https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory"
    URL = "https://api.live.bilibili.com/msg/send"
    ROOM_URL = "https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom"
    CONF_URL = "https://api.live.bilibili.com/room/v1/Danmu/getConf"

    def __init__(self, config):
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

    def start(self):
        self.get_room_info()
        self.get_room_conf()
        self.get_db_connect()
        self.get_socket_connect()
        self.get_danmu()

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
            for data in DanMuJi.unpack_packets(brotli.decompress(message)):
                yield data
        else:
            yield version, msg_type, message

    def get_danmu(self):
        def get():
            while True:
                for data in self.socket_recv():
                    self.deal(*data)
        self._thread = threading.Thread(target=get, daemon=True)
        self._thread.start()

    def deal(self, version, msg_type, data):
        if msg_type == TYPE_SERVER_AUTH:
            print("服务器认证通过")
        elif msg_type == TYPE_SERVER_HEARTBEAT:
            if version == VERSION_HEARTBEAT:
                print("当前房间内人数", int.from_bytes(data, 'big'))
        elif msg_type == TYPE_SERVER_INFO:
            data = json.loads(data)
            cmd = data.get("cmd")
            if cmd == "STOP_LIVE_ROOM_LIST" or "NOTICE_MSG":
                print(data)
            elif cmd == "DANMU_MSG":
                info = data.get("info")
                content = info[1]
                user_info = info[2]
                medal_info = info[3]
                print(content, user_info, medal_info)
            elif cmd == "ONLINE_RANK_COUNT":
                print("高能榜人数:", data["data"]["count"])
            elif cmd == "ONLINE_RANK_V2":
                print(data["data"]["list"])
            elif cmd == "WATCHED_CHANGE":
                print(data["data"]["text_large"])
            else:
                print(data)
            
    # def get(self):
    #     response = requests.get(url=self.GET_URL, headers=self.headers, params={"roomid": self.roomid})
    #     datapack = json.loads(response.content)
    #     cards = heapq.merge(datapack["data"]["admin"] + datapack["data"]["room"], key=lambda x: x["check_info"]["ts"])
    #     for card in cards:
    #         d = DanMu(**card)
    #         if d not in self._cache:
    #             print(d)
    #             self._cache.add(d)
    #             self.save(d)

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
        response = requests.post(self.URL, data=data, cookies={"Cookie": self.cookies})
        result = json.loads(response.content)
        if result["code"] != 0:
            print(f"发送【{msg}】失败")

    def save(self, danmu):
        keys = ','.join(danmu.keys())
        values = ','.join(["?"] * len(danmu))
        self._cursor.execute(f"""INSERT OR IGNORE INTO "danmu" ({keys}) VALUES ({values})""", tuple(danmu.values()))
        self._connect.commit()

    def stop(self):
        self._heartbeat.cancel()
        self._connect.close()


if __name__ == "__main__":
    c = DanMuJi(CONFIG)
    c.start()

    atexit.register(c.stop)
