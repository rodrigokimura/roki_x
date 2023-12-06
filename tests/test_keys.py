from unittest.mock import patch

import pytest
from adafruit_hid.mouse import Mouse

from firmware.config import Config
from firmware.keys import KeyWrapper, init, sender_map


@pytest.fixture
def mock_config():
    return Config()


def test_sender_map_not_initialised():
    assert sender_map == {}


def test_init(mock_config: Config):
    init(mock_config)
    from firmware.keys import sender_map

    assert sender_map != {}


def test_key_wrapper(mock_config: Config):
    init(mock_config)

    k = KeyWrapper(["a", "b"])
    k.press_and_release()
    k = KeyWrapper("a")
    k.press_and_release()
    k = KeyWrapper("volume_up")
    k.press_and_release()
    k = KeyWrapper()
    k.press_and_release()
    k = KeyWrapper("layer_1_hold")
    k.press_and_release()


def test_key_wrapper_mouse_button(mock_config: Config):
    init(mock_config)

    with patch.object(Mouse, "press") as m:
        k = KeyWrapper("left_button")
        k.press_and_release()

        m.assert_called_once()


def test_key_wrapper_mouse_movement(mock_config: Config):
    init(mock_config)

    with patch.object(Mouse, "move") as m:
        for d in ("up", "down", "left", "right"):
            k = KeyWrapper(f"mouse_move_{d}")
            k.press_and_release()

        for d in ("up", "down"):
            k = KeyWrapper(f"mouse_scroll_{d}")
            k.press_and_release()

        m.assert_called()
        assert m.call_count == 6
