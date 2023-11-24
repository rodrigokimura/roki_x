import json

from adafruit_hid.consumer_control_code import ConsumerControlCode as MediaKey
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse


def get_all_keys():
    return [
        n
        for c in [Keycode, MediaKey, Mouse]
        for n in sorted(
            (
                a
                for a in dir(c)
                if not a.startswith("_") and not callable(getattr(c, a))
            ),
            key=lambda a: getattr(c, a),
        )
    ]


if __name__ == "__main__":
    all_keys = get_all_keys()
    result = json.dumps(all_keys)
    print(result)
