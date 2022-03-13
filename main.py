import json
import heapq
import random

import sqlite3
import requests
import threading
import atexit


from items import DanMu
from config import CONFIG


class DanMuJi:
    GET_URL = "https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory"
    SEND_URL = "https://api.live.bilibili.com/msg/send"
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

    def start(self):
        self.get_room_info()
        self.get_room_conf()
        self.get_db_connect()
        self.get_danmu()

    def get_room_info(self):
        response = requests.get(self.ROOM_URL, headers=self.headers, params={"room_id": self.roomid})
        data = json.loads(response.content).get("data")
        assert data
        room_info = data["room_info"]
        self._uid = room_info["uid"]
        self._nickname = data["anchor_info"]["base_info"]["uname"]
        self._roomid = room_info["roomid"]
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

    def get_danmu(self):
        try:
            self.get()
        except Exception as e:
            pass
        self.thread = threading.Timer(1, self.get_danmu)
        self.thread.daemon = True
        self.thread.start()

    def get(self):
        response = requests.get(url=self.GET_URL, headers=self.headers, params={"roomid": self.roomid})
        datapack = json.loads(response.content)
        cards = heapq.merge(datapack["data"]["admin"] + datapack["data"]["room"], key=lambda x: x["check_info"]["ts"])
        for card in cards:
            d = DanMu(**card)
            if d not in self._cache:
                print(d)
                self._cache.add(d)
                self.save(d)

    def send(self, msg):
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
        if result["code"] != 0:
            print(f"发送【{msg}】失败")

    def save(self, danmu):
        self.insert("danmu", danmu)

    def insert(self, tablename, item):
        keys = ','.join(item.keys())
        values = ','.join(["?"] * len(item))
        self._cursor.execute(f"""INSERT OR IGNORE INTO {tablename} ({keys}) VALUES ({values})""", tuple(item.values()))
        self._connect.commit()

    def stop(self):
        self.thread.cancel()
        self._connect.close()


if __name__ == "__main__":
    c = DanMuJi(CONFIG)
    c.start()

    atexit.register(c.stop)
