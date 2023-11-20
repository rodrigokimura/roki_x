import sys
from unittest.mock import MagicMock

board = MagicMock()
busio = MagicMock()
keypad = MagicMock()
keypad.KeyMatrix = MagicMock()
adafruit_hid = MagicMock()
adafruit_hid_consumer_control = MagicMock()


class MockDevice:
    def __init__(self, _) -> None:
        ...


class MockMedia(MockDevice):
    def send(self, _):
        ...


class MockKeyboard(MockDevice):
    def press(self, _):
        ...

    def release(self, _):
        ...


class MockMouse(MockDevice):
    LEFT_BUTTON = 0

    def click(self, _):
        ...


class MockKeycode:
    A = 0
    B = 1
    C = 2


class MockMediaKey:
    VOLUME_UP = 0


adafruit_hid_consumer_control.ConsumerControl = MockMedia

adafruit_hid_consumer_control_code = MagicMock()
adafruit_hid_consumer_control_code.ConsumerControlCode = MockMediaKey
adafruit_hid_keyboard = MagicMock()
adafruit_hid_keyboard.Keyboard = MockKeyboard

adafruit_hid_keycode = MagicMock()
adafruit_hid_keycode.Keycode = MockKeycode
adafruit_hid_mouse = MagicMock()
adafruit_hid_mouse.Mouse = MockMouse

neopixel = MagicMock()
supervisor = MagicMock()
i2ctarget = MagicMock()
usb_hid = MagicMock()

sys.modules["board"] = board
sys.modules["busio"] = busio
sys.modules["keypad"] = keypad
sys.modules["adafruit_hid"] = adafruit_hid
sys.modules["adafruit_hid.consumer_control"] = adafruit_hid_consumer_control
sys.modules["adafruit_hid.consumer_control_code"] = adafruit_hid_consumer_control_code
sys.modules["adafruit_hid.keyboard"] = adafruit_hid_keyboard
sys.modules["adafruit_hid.keycode"] = adafruit_hid_keycode
sys.modules["adafruit_hid.mouse"] = adafruit_hid_mouse
sys.modules["neopixel"] = neopixel
sys.modules["supervisor"] = supervisor
sys.modules["i2ctarget"] = i2ctarget
sys.modules["usb_hid"] = usb_hid
