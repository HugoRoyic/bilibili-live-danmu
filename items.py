import datetime


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
