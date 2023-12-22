try:
    from typing import TYPE_CHECKING as __t

    TYPE_CHECKING = __t
except ImportError:  # pragma: no cover
    TYPE_CHECKING = False


def parse_color(
    color: str | list[int | str] | tuple[int | str, int | str, int | str]
) -> tuple[int, int, int]:
    if isinstance(color, str):
        if color[0] == "#":
            color = color[1:]
        if len(color) != 6:
            raise ValueError("Invalid color")
        r = color[:2]
        g = color[2:4]
        b = color[4:]
        return int(r, 16), int(g, 16), int(b, 16)

    if isinstance(color, (list, tuple)):
        return int(color[0]), int(color[1]), int(color[2])

    raise NotImplementedError


def to_int(bools: list[bool]):
    return sum(b << i for i, b in enumerate(bools))


def from_int(i: int, size=6):
    return [bool((i >> j) & 1) for j in range(size)]


def to_bytes(bools: list[list[bool]]):
    return bytes(to_int(b) for b in bools)


def from_bytes(b: bytes):
    return [from_int(i) for i in b]


def get_coords(i: int, col_count: int = 6):
    c = i % col_count
    r = i // col_count
    return r, c


def diff_bitmaps(a: bytearray, b: bytearray, byte_size=6):
    for r, (x, y) in enumerate(zip(a, b)):
        for c in range(byte_size):
            if ((x >> c) & 1) != (value := ((y >> c) & 1)):
                yield (r, c), bool(value)
