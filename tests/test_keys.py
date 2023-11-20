from itertools import cycle
from unittest.mock import patch

import pytest

from keys import KeyWrapper, get_opts, init, sender_map


@pytest.fixture
def mock_get_opts():
    with patch("keys.get_opts", side_effect=cycle([{"A"}, {"B"}, {"C"}])) as m:
        yield m


def test_get_opts():
    class MockClient:
        A = 1
        _B = 2

    assert get_opts(MockClient) == {"A"}


def test_sender_map_not_initialised():
    assert sender_map == {}


def test_init():
    init()
    from keys import sender_map

    assert sender_map != {}


def test_key_wrapper():
    init()
    k = KeyWrapper("a")
    k.press_and_release()
    k = KeyWrapper("left_button")
    k.press_and_release()
    k = KeyWrapper("volume_up")
    k.press_and_release()
