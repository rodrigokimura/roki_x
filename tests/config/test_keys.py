from config.keys import KEYBOARD_KEYS, KEYS, MEDIA_KEYS, MOUSE_KEYS


def test_keys():
    assert len(KEYBOARD_KEYS) == 129
    assert len(MEDIA_KEYS) == 13
    assert len(MOUSE_KEYS) == (
        3  # for buttons
        + 4  # for cursor direction ["up", "down", "left", "right"]
        + 2  # for scroll wheel ["up", "down"]
    )
    assert len(KEYS) == sum([len(KEYBOARD_KEYS), len(MEDIA_KEYS), len(MOUSE_KEYS)])
    assert len(set(KEYS)) == len(KEYS)
