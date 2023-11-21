import pytest

from config import Config
from keys import KeyWrapper, init, sender_map


@pytest.fixture
def mock_config():
    return Config()


def test_sender_map_not_initialised():
    assert sender_map == {}


def test_init(mock_config: Config):
    init(mock_config)
    from keys import sender_map

    assert sender_map != {}


def test_key_wrapper(mock_config: Config):
    init(mock_config)
    k = KeyWrapper("a")
    k.press_and_release()
    k = KeyWrapper("left_button")
    k.press_and_release()
    k = KeyWrapper("volume_up")
    k.press_and_release()
    k = KeyWrapper()
    k.press_and_release()
    k = KeyWrapper("layer_1_hold")
    k.press_and_release()
