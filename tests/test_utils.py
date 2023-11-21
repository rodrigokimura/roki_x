import pytest

from utils import (
    diff_bitmaps,
    from_bytes,
    from_int,
    get_coords,
    parse_color,
    to_bytes,
    to_int,
)


def test_get_coords():
    r = get_coords(0)
    assert r == (0, 0)

    r = get_coords(1)
    assert r == (0, 1)

    r = get_coords(6)
    assert r == (1, 0)

    r = get_coords(16)
    assert r == (2, 4)


def test_diff_bitmaps():
    a = to_bytes(
        [
            [False, False, False, False, False, False],
            [False, False, True, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
        ]
    )
    b = to_bytes(
        [
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, True, False],
            [False, False, False, False, False, False],
        ]
    )
    r = diff_bitmaps(bytearray(a), bytearray(b))

    assert list(r) == [((1, 2), False), ((3, 4), True)]


def test_to_int():
    r = to_int([False, False, False, False, False, False])
    assert r == 0
    r = to_int([True, False, True, False, False, False])
    assert r == 5


def test_from_int():
    r = from_int(0)
    assert r == [False, False, False, False, False, False]
    r = from_int(5)
    assert r == [True, False, True, False, False, False]


def test_to_bytes():
    r = to_bytes(
        [
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, True, False],
            [False, False, False, False, False, False],
        ]
    )
    assert r == b"\x00\x00\x00\x10\x00"


def test_from_bytes():
    r = from_bytes(b"\x00\x00\x00\x10\x00")
    assert r == [
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, True, False],
        [False, False, False, False, False, False],
    ]


def test_parse_color():
    r = parse_color("#000000")
    assert r == (0, 0, 0)
    r = parse_color("000000")
    assert r == (0, 0, 0)
    r = parse_color([0, 0, 0])
    assert r == (0, 0, 0)
    r = parse_color((0, 0, 0))
    assert r == (0, 0, 0)
    with pytest.raises(ValueError):
        parse_color("not-a-color")
    with pytest.raises(NotImplementedError):
        parse_color({})  # type: ignore
