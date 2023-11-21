import asyncio
import time

import board
import busio
import neopixel
import supervisor  # type: ignore
from adafruit_bus_device.i2c_device import I2CDevice
from i2ctarget import I2CTarget  # type: ignore
from keypad import KeyMatrix

from config import Config
from utils import diff_bitmaps, get_coords, parse_color, to_bytes

ROW_PINS = (11, 15)
COL_PINS = (16, 21)


class RokiX:
    def __init__(self, i2c_device_id: int) -> None:
        self._pixels = neopixel.NeoPixel(board.GP23, 1)  # type: ignore
        self._pixels.brightness = 0.1
        self.i2c_device_id = i2c_device_id

        self.i2c_scl_pin = board.GP1  # type: ignore
        self.i2c_sda_pin = board.GP0  # type: ignore

        self.neopixel = parse_color("#ffff00")
        self._primary: bool | None = None

        row_start, row_end = ROW_PINS
        col_start, col_end = COL_PINS

        self.rows = tuple(
            getattr(board, f"GP{i}") for i in range(row_start, row_end + 1)
        )
        self.cols = tuple(
            getattr(board, f"GP{i}") for i in range(col_start, col_end + 1)
        )

        self.curr_bitmap = bytearray(len(self.rows))
        self.last_bitmap = bytearray(len(self.rows))

        self.key_matrix = KeyMatrix(
            row_pins=self.rows, column_pins=self.cols, columns_to_anodes=False
        )
        self.matrix_buffer = [[False] * len(self.cols) for _ in self.rows]

        if self.primary:
            # TODO: check why this doesn't work on the secondary side
            self.config = Config.read()

    @property
    def primary(self):
        if self._primary is None:
            # call to supervisor.runtime.usb_connected needs time to work
            time.sleep(1)
            self._primary = supervisor.runtime.usb_connected
        return self._primary

    @property
    def neopixel(self):
        return self._pixels[0]

    @neopixel.setter
    def neopixel(self, value):
        self._pixels[0] = value

    async def run(self):
        if self.primary:
            await self.run_as_primary()
        else:
            await self.run_as_secondary()

    @property
    def layer(self):
        return self.config.layer

    async def run_as_primary(self):
        with busio.I2C(scl=self.i2c_scl_pin, sda=self.i2c_sda_pin) as i2c:  # type: ignore
            with I2CDevice(i2c, self.i2c_device_id, False) as device:  # type: ignore
                self.neopixel = parse_color("#00ffff")
                await asyncio.sleep(1)
                while True:
                    event = self.key_matrix.events.get()
                    if event:
                        row, col = get_coords(event.key_number, len(self.cols))
                        key = self.layer.primary_keys[row][col]
                        print(key.key_names)
                        (key.press if event.pressed else key.release)()

                    device.readinto(self.curr_bitmap, end=len(self.rows))
                    if self.curr_bitmap:
                        self.neopixel = parse_color("#0000ff")
                    else:
                        self.neopixel = parse_color("#ff0000")

                    for (row, col), pressed in diff_bitmaps(
                        self.last_bitmap, self.curr_bitmap
                    ):
                        key = self.layer.secondary_keys[row][col]
                        print(key.key_names)
                        (key.press if pressed else key.release)()
                    self.last_bitmap[:] = self.curr_bitmap

    async def run_as_secondary(self):
        with I2CTarget(  # type: ignore
            self.i2c_scl_pin, self.i2c_sda_pin, (self.i2c_device_id,)
        ) as device:
            self.neopixel = parse_color("#00ffff")
            await asyncio.sleep(1)
            while True:
                event = self.key_matrix.events.get()
                if event:
                    row, col = get_coords(event.key_number, len(self.cols))
                    self.matrix_buffer[row][col] = event.pressed
                if request := device.request():
                    with request:  # type: ignore
                        if request.address == self.i2c_device_id:
                            if not request.is_read:
                                # TODO: add logic to receive layer
                                request.read(1)
                            elif request.is_restart:
                                pass
                            else:
                                self.neopixel = parse_color("#00ff00")
                                request.write(to_bytes(self.matrix_buffer))
