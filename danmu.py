import json
import heapq
import random
import sqlite3
import datetime
import requests
import threading
import atexit


class Field:
    pass


class ItemMeta(type):
    def __new__(mcs, cls, bases, attrs):
        fields = []
        for key in attrs:
            value = attrs[key]
            if isinstance(value, Field):
                fields.append(key)

        attrs["fields"] = fields
        return type.__new__(mcs, cls, bases, attrs)


class Item(metaclass=ItemMeta):
    def __init__(self):
        super().__init__()
        self._values = {}

    def __getitem__(self, key):
        return self._values[key]

    def __setitem__(self, key, value):
        assert key in self.fields
        self._values[key] = value

    def __len__(self):
        return len(self._values)

    def keys(self):
        return self._values.keys()

    def values(self):
        return self._values.values()


class DanMu(Item):
    ts = Field()
    ct = Field()
    uid = Field()
    nickname = Field()
    text = Field()
    date = Field()
    time = Field()

    def __init__(self, **kwargs):
        super().__init__()
        self["ts"] = kwargs["check_info"]["ts"]
        self["ct"] = int(kwargs["check_info"]["ct"], 16)
        self["text"] = kwargs.get("text")
        self["uid"] = kwargs.get("uid")
        self["nickname"] = kwargs.get("nickname")

        timeline = kwargs.get("timeline") or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self["date"], self["time"] = timeline.split()


    def __eq__(self, obj):
        return self["ts"] == obj["ts"] and self["ct"] == obj["ct"]

    def __hash__(self):
        return self["ct"]

    def __str__(self):
        return f"""{self["date"]} {self["time"]} | {self["nickname"]}: {self["text"]}"""


class DanMuJi:
    GET_URL = "https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory"
    SEND_URL = "https://api.live.bilibili.com/msg/send"

    def __init__(self, config):
        self.headers = config.get("headers")
        self.roomid = config.get("roomid")
        self.cookies = config.get("cookies")
        self.csrf = config.get("csrf")

        self.cache = set()

        self.connect = sqlite3.connect(f'history-{self.roomid}.db', check_same_thread=False)
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
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

    def start(self):
        self.get()
        self.thread = threading.Timer(1, self.start)
        self.thread.daemon = True
        self.thread.start()

    def get(self):
        response = requests.get(url=self.GET_URL, headers=self.headers, params={"roomid": self.roomid})
        datapack = json.loads(response.content)
        cards = heapq.merge(datapack["data"]["admin"] + datapack["data"]["room"], key=lambda x: x["check_info"]["ts"])
        for card in cards:
            d = DanMu(**card)
            if d not in self.cache:
                print(d)
                self.cache.add(d)
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
        self.cursor.execute(f"""INSERT OR IGNORE INTO {tablename} ({keys}) VALUES ({values})""", tuple(item.values()))
        self.connect.commit()

    def stop(self):
        self.thread.cancel()
        self.connect.close()


if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)

    c = DanMuJi(config)
    c.start()

    atexit.register(c.stop)