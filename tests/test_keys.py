from unittest.mock import patch

import pytest
from adafruit_hid.consumer_control import ConsumerControl as Media
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse

from firmware.config import Config
from firmware.keys import KeyWrapper, sender_map
from firmware.manager import Manager


@pytest.fixture
def mock_config():
    return Config()


def test_sender_map_not_initialised():
    assert sender_map == {}


@pytest.mark.usefixtures("mock_config")
def test_config_initialization_should_hydrate_sender_map():
    from firmware.keys import sender_map

    assert sender_map != {}


@pytest.mark.usefixtures("mock_config")
def test_key_wrapper_keyboard():
    with patch.object(Keyboard, "press") as m:
        KeyWrapper("a").press_and_release()

        m.assert_called_once()


@pytest.mark.usefixtures("mock_config")
def test_key_wrapper_media():
    with patch.object(Media, "press") as m:
        KeyWrapper("volume_up").press_and_release()

        m.assert_called_once()


@pytest.mark.usefixtures("mock_config")
def test_key_wrapper_mouse_button():
    with patch.object(Mouse, "press") as m:
        KeyWrapper("left_button").press_and_release()

        m.assert_called_once()


@pytest.mark.usefixtures("mock_config")
def test_key_wrapper_multiple():
    with (
        patch.object(Media, "press") as media,
        patch.object(Keyboard, "press") as keyboard,
    ):
        KeyWrapper(["a", "volume_up"]).press_and_release()

        media.assert_called_once()
        keyboard.assert_called_once()


@pytest.mark.usefixtures("mock_config")
def test_key_wrapper_noop():
    with (
        patch.object(Media, "press") as media,
        patch.object(Keyboard, "press") as keyboard,
        patch.object(Mouse, "press") as mouse,
        patch.object(Manager, "on_press") as manager,
    ):
        KeyWrapper().press_and_release()

        keyboard.assert_not_called()
        media.assert_not_called()
        mouse.assert_not_called()
        manager.assert_not_called()


def test_key_wrapper_layer_hold(mock_config: Config):
    current_layer = mock_config.layer_index

    KeyWrapper("layer_1_hold").press()
    assert mock_config.layer_index == 1

    KeyWrapper("layer_1_hold").release()
    assert mock_config.layer_index == current_layer


def test_key_wrapper_layer_press(mock_config: Config):
    current_layer = mock_config.layer_index

    KeyWrapper("layer_2_press").press()
    assert current_layer != mock_config.layer_index
    assert mock_config.layer_index == 2

    KeyWrapper("layer_2_press").release()
    assert mock_config.layer_index == 2


@pytest.mark.usefixtures("mock_config")
def test_key_wrapper_mouse_movement():
    with patch.object(Mouse, "move") as mouse:
        for d in ("up", "down", "left", "right"):
            KeyWrapper(f"mouse_move_{d}").press_and_release()

        for d in ("up", "down"):
            KeyWrapper(f"mouse_scroll_{d}").press_and_release()

        mouse.assert_called()
        assert mouse.call_count == 6
