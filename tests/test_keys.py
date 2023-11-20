from itertools import cycle
from unittest.mock import patch

from keys import KeyWrapper, get_opts, init, sender_map


def test_get_opts():
    class MockClient:
        A = 1
        _B = 2

    assert get_opts(MockClient) == {"A"}


def test_sender_map_not_initialised():
    assert sender_map == {}


@patch("keys.get_opts", side_effect=cycle([{"A"}, {"B"}, {"C"}]))
def test_init(m):
    init()
    from keys import sender_map

    assert sender_map != {}


@patch("keys.get_opts", side_effect=cycle([{"A"}, {"B"}, {"C"}]))
def test_key_wraper(m):
    init()
    from keys import sender_map

    k = KeyWrapper("a")
    k.press()
    print(k)
