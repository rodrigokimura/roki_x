import json

from keys import KeyWrapper
from utils import parse_color


class Layer:
    name: str
    color: tuple[int, int, int]
    primary_keys: tuple[tuple[KeyWrapper, ...], ...]
    secondary_keys: tuple[tuple[KeyWrapper, ...], ...]

    @classmethod
    def from_dict(cls, data: dict):
        i = cls()
        i.name = data.get("name", "no name")
        c = data.get("color", "#000000")
        i.color = parse_color(c)
        i.primary_keys = tuple(
            tuple(reversed([KeyWrapper(k) for k in row]))
            for row in data.get("primary_keys", (("",),))
        )
        i.secondary_keys = tuple(
            tuple(reversed([KeyWrapper(k) for k in row]))
            for row in data.get("secondary_keys", (("",),))
        )
        return i


class Config:
    layers: list[Layer]

    @classmethod
    def read(cls):
        with open("config.json") as file:
            config = json.load(file)
        i = cls()
        i.layers = [Layer.from_dict(layer) for layer in config.get("layers", {})]
        return i
