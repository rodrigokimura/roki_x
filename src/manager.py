from __future__ import annotations

from utils import TYPE_CHECKING

if TYPE_CHECKING:
    from config import Config


class Manager:
    def __init__(self, c: Config) -> None:
        self._prev = 0
        self.config = c

    def on_press(self, c: Command):
        if c.index != self.config.layer_index:
            self._prev = self.config.layer_index
        self.config.layer_index = c.index

    def on_release(self, c: Command):
        if c.type_ == "hold":
            self.config.layer_index = self._prev


class Commands:
    def __getattribute__(self, __name: str):
        if not __name.lower().startswith("layer_"):
            return Command()

        _, index, type_ = __name.split("_")
        return Command(int(index), type_)

    def get(self, n):
        return self.__getattribute__(n)

    def __contains__(self, n):
        return str(n).lower().startswith("layer_")


class Command:
    def __init__(self, index: int = 0, type_: str | None = None) -> None:
        self.index = index
        if not type_:
            self.type_ = None
        elif type_.lower() not in ("press", "hold"):
            self.type_ = None
        else:
            self.type_ = type_.lower()
