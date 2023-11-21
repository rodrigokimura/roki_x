from __future__ import annotations

from utils import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
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
    def get(self, __name: str) -> Command:
        if __name.lower().startswith("layer_"):
            _, index, type_ = __name.split("_")
            return Command(int(index), type_)
        return Command()

    def __contains__(self, n: str) -> bool:
        return n.lower().startswith("layer_")


class Command:
    def __init__(self, index: int = 0, type_: str | None = None) -> None:
        self.index = index
        if not type_:
            self.type_ = None
        elif type_.lower() not in ("press", "hold"):
            self.type_ = None
        else:
            self.type_ = type_.lower()
