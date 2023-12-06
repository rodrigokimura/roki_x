from unittest.mock import patch

import pytest
from adafruit_hid.consumer_control import ConsumerControl as Media
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse

from firmware.config import Config
from firmware.keys import KeyWrapper, init, sender_map
from firmware.manager import Manager


@pytest.fixture
def mock_config():
    return Config()


def test_sender_map_not_initialised():
    assert sender_map == {}


def test_init(mock_config: Config):
    init(mock_config)
    from firmware.keys import sender_map

    assert sender_map != {}


def test_key_wrapper_keyboard(mock_config: Config):
    init(mock_config)

    with patch.object(Keyboard, "press") as m:
        k = KeyWrapper("a")
        k.press_and_release()

        m.assert_called_once()


def test_key_wrapper_media(mock_config: Config):
    init(mock_config)

    with patch.object(Media, "press") as m:
        k = KeyWrapper("volume_up")
        k.press_and_release()

        m.assert_called_once()


def test_key_wrapper_mouse_button(mock_config: Config):
    init(mock_config)

    with patch.object(Mouse, "press") as m:
        k = KeyWrapper("left_button")
        k.press_and_release()

        m.assert_called_once()


def test_key_wrapper_multiple(mock_config: Config):
    init(mock_config)

    with patch.object(Media, "press") as mm, patch.object(Keyboard, "press") as mk:
        k = KeyWrapper(["a", "volume_up"])
        k.press_and_release()

        mm.assert_called_once()
        mk.assert_called_once()


def test_key_wrapper_noop(mock_config: Config):
    init(mock_config)

    with (
        patch.object(Media, "press") as media,
        patch.object(Keyboard, "press") as keyboard,
        patch.object(Mouse, "press") as mouse,
        patch.object(Manager, "on_press") as manager,
    ):
        k = KeyWrapper()
        k.press_and_release()

        keyboard.assert_not_called()
        media.assert_not_called()
        mouse.assert_not_called()
        manager.assert_not_called()


def test_key_wrapper_layer(mock_config: Config):
    init(mock_config)

    with patch.object(Manager, "on_press") as manager:
        k = KeyWrapper("layer_1_hold")
        k.press_and_release()

        manager.assert_called_once()


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
