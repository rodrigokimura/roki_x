from utils import diff_bitmaps, diff_matrices, get_coords, to_bytes


def test_get_coords():
    r = get_coords(0)
    assert r == (0, 0)

    r = get_coords(1)
    assert r == (0, 1)

    r = get_coords(6)
    assert r == (1, 0)

    r = get_coords(16)
    assert r == (2, 4)


def test_diff():
    a = [[False, True], [False, False]]
    b = [[False, False], [False, True]]
    r = diff_matrices(a, b)

    assert list(r) == [((0, 1), False), ((1, 1), True)]


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
