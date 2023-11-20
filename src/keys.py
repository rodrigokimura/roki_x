import usb_hid
from adafruit_hid.consumer_control import ConsumerControl as Media
from adafruit_hid.consumer_control_code import ConsumerControlCode as MediaKey
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

try:
    from typing import TYPE_CHECKING
except ImportError:
    TYPE_CHECKING = False

if TYPE_CHECKING:
    Device = Keyboard | Mouse | Media
    Codes = Keycode | Mouse | MediaKey


def get_opts(cls: type[object]):
    return {
        k for k, v in cls.__dict__.items() if not k.startswith("_") and not callable(v)
    }


sender_map: dict[Device, tuple[type[Codes], set[str]]] = {}


def init():
    global sender_map
    sender_map = {
        Keyboard(usb_hid.devices): (Keycode, get_opts(Keycode)),
        Mouse(usb_hid.devices): (Mouse, get_opts(Mouse)),
        Media(usb_hid.devices): (MediaKey, get_opts(MediaKey)),
    }
    union_all = set()
    for _, s in sender_map.values():
        union_all |= s

    assert sum(len(s) for _, s in sender_map.values()) == len(
        union_all
    ), "Overlapping constant names"


class KeyWrapper:
    __slot__ = ("key_names", "params")

    def __init__(self, keys: str | list[str]) -> None:
        global sender_map
        if isinstance(keys, str):
            keys = [keys.upper()]
        else:
            keys = [key.upper() for key in keys]

        self.key_names = keys
        self.params = tuple(
            (sender, getattr(key_container, key))
            for sender, (key_container, key_set) in sender_map.items()
            for key in keys
            if key in key_set
        )

    def _press(self, sender, key_code):
        if isinstance(sender, Media):
            sender.send(key_code)
        elif isinstance(sender, Keyboard):
            sender.press(key_code)
        elif isinstance(sender, Mouse):
            sender.click(key_code)

    def _release(self, sender, key_code):
        if isinstance(sender, Media):
            pass
        elif isinstance(sender, Keyboard):
            sender.release(key_code)
        elif isinstance(sender, Mouse):
            pass

    def press(self):
        for sender, key_code in self.params:
            self._press(sender, key_code)

    def release(self):
        for sender, key_code in self.params:
            self._release(sender, key_code)

    def press_and_release(self):
        self.press()
        self.release()
