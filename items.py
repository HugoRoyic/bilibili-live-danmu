from typing import overload


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
    uid = Field()
    nickname = Field()
    text = Field()
    date = Field()
    time = Field()

    def __init__(self, **kwargs):
        super().__init__()
        for key in kwargs:
            self[key] = kwargs[key]

    def __eq__(self, obj):
        return self["ts"] == obj["ts"] and self["ct"] == obj["ct"]

    def __str__(self):
        return f"""{self["date"]} {self["time"]} | {self["nickname"]}: {self["text"]}"""
