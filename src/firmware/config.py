from __future__ import annotations

import json
import os

from firmware.keys import KeyWrapper, init
from firmware.utils import parse_color


class Layer:
    name: str
    color: tuple[int, int, int]
    primary_keys: tuple[tuple[KeyWrapper, ...], ...]
    secondary_keys: tuple[tuple[KeyWrapper, ...], ...]

    @classmethod
    def from_dict(cls, data: dict) -> Layer:
        is_left_side = bool(os.getenv("IS_LEFT_SIDE", True))
        i = cls()
        i.name = data.get("name", "no name")
        c = data.get("color", "#000000")
        i.color = parse_color(c)
        i.primary_keys = tuple(
            tuple(reversed([KeyWrapper(k) for k in row]))
            for row in data.get(
                "primary_keys" if is_left_side else "secondary_keys", (("",),)
            )
        )
        i.secondary_keys = tuple(
            tuple(reversed([KeyWrapper(k) for k in row]))
            for row in data.get(
                "secondary_keys" if is_left_side else "primary_keys", (("",),)
            )
        )
        return i


class Config:
    layers: tuple[Layer, ...]
    autoreload: bool

    def __init__(
        self, layers: list[dict] | None = None, autoreload: bool = False
    ) -> None:
        init(self)
        self.layer_index = 0
        self.layers = tuple(Layer.from_dict(layer) for layer in layers or tuple())
        self.autoreload = autoreload

    @property
    def layer(self):
        return self.layers[self.layer_index]

    @classmethod
    def read(cls):
        with open("config.json") as file:
            config: dict = json.load(file)
        return cls(
            layers=config.get("layers", []),
            autoreload=config.get("autoreload", False),
        )
