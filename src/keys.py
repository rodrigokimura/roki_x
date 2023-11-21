from __future__ import annotations

import usb_hid
from adafruit_hid.consumer_control import ConsumerControl as Media
from adafruit_hid.consumer_control_code import ConsumerControlCode as MediaKey
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

from manager import Commands, Manager
from utils import TYPE_CHECKING


class KeyboardCode:
    def get(self, n):
        return getattr(Keycode, n)

    def __contains__(self, n):
        return hasattr(Keycode, n)


class MouseButton:
    def get(self, n):
        return getattr(Mouse, n)

    def __contains__(self, n):
        return hasattr(Mouse, n)


class MediaFunction:
    def get(self, n):
        return getattr(MediaKey, n)

    def __contains__(self, n):
        return hasattr(MediaKey, n)


if TYPE_CHECKING:
    from config import Config

    Device = Keyboard | Mouse | Media | Manager
    Code = KeyboardCode | MouseButton | MediaFunction | Commands


def get_opts(cls: type[object]):
    return {
        k for k, v in cls.__dict__.items() if not k.startswith("_") and not callable(v)
    }


sender_map: dict[Device, Code] = {}


def init(c: Config):
    global sender_map
    sender_map = {
        Keyboard(usb_hid.devices): KeyboardCode(),
        Mouse(usb_hid.devices): MouseButton(),
        Media(usb_hid.devices): MediaFunction(),
        Manager(c): Commands(),
    }


class KeyWrapper:
    def __init__(self, keys: str | list[str]) -> None:
        global sender_map
        if isinstance(keys, str):
            keys = [keys.upper()]
        else:
            keys = [key.upper() for key in keys]

        self.key_names = keys
        self.params = tuple(
            (sender, key_container.get(key))
            for sender, key_container in sender_map.items()
            for key in keys
            if key in key_container
        )

    def _press(self, sender, key_code):
        if isinstance(sender, Media):
            sender.send(key_code)
        elif isinstance(sender, Keyboard):
            sender.press(key_code)
        elif isinstance(sender, Mouse):
            sender.click(key_code)
        elif isinstance(sender, Manager):
            sender.on_press(key_code)

    def _release(self, sender, key_code):
        if isinstance(sender, Media):
            pass
        elif isinstance(sender, Keyboard):
            sender.release(key_code)
        elif isinstance(sender, Mouse):
            pass
        elif isinstance(sender, Manager):
            sender.on_release(key_code)

    def press(self):
        for sender, key_code in self.params:
            self._press(sender, key_code)

    def release(self):
        for sender, key_code in self.params:
            self._release(sender, key_code)

    def press_and_release(self):
        self.press()
        self.release()
