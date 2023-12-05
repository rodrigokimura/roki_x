import asyncio
import os
import time

import board
import busio
import digitalio
import neopixel
import supervisor  # type: ignore
from adafruit_bus_device.i2c_device import I2CDevice
from i2ctarget import I2CTarget  # type: ignore
from keypad import KeyMatrix
from microcontroller import watchdog as _watchdog
from watchdog import WatchDogMode  # type: ignore

from firmware.config import Config, Layer
from firmware.utils import diff_bitmaps, get_coords, parse_color, to_bytes

ROW_PINS = (11, 15)
COL_PINS = (16, 21)

# colors
INITIAL = parse_color("#ffff00")
I2C_SET = parse_color("#00ffff")


class RokiX:
    def __init__(self, i2c_device_id: int) -> None:
        led = digitalio.DigitalInOut(board.GP25)  # type: ignore
        led.direction = digitalio.Direction.OUTPUT

        if _watchdog is not None:
            self.watchdog = _watchdog
            self.watchdog.timeout = 5
            self.watchdog.mode = WatchDogMode.RESET

        self._pixels = neopixel.NeoPixel(board.GP23, 1)  # type: ignore
        self._pixels.brightness = 0.1
        self.i2c_device_id = i2c_device_id

        self.i2c_scl_pin = board.GP1  # type: ignore
        self.i2c_sda_pin = board.GP0  # type: ignore

        self.neopixel = INITIAL
        self._primary: bool | None = None
        self._prev_layer_index: int = 0

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
            led.value = bool(os.getenv("IS_LEFT_SIDE", True))

    @property
    def primary(self) -> bool:
        if self._primary is None:
            # call to supervisor.runtime.usb_connected needs time to work
            time.sleep(1)
            self._primary = supervisor.runtime.usb_connected
        return self._primary

    @property
    def neopixel(self):
        return self._pixels[0]

    @neopixel.setter
    def neopixel(self, value: tuple[int, int, int]) -> None:
        if len(value) == 3:
            self._pixels[0] = value

    async def run(self):
        while True:
            try:
                if self.primary:
                    await self.run_as_primary()
                else:
                    await self.run_as_secondary()
            except KeyboardInterrupt:
                exit()
            except Exception:
                pass

    @property
    def layer(self) -> Layer:
        return self.config.layer

    async def run_as_primary(self) -> None:
        with busio.I2C(scl=self.i2c_scl_pin, sda=self.i2c_sda_pin) as i2c:  # type: ignore
            with I2CDevice(i2c, self.i2c_device_id, False) as device:  # type: ignore
                self.neopixel = I2C_SET
                await asyncio.sleep(1)
                while True:
                    event = self.key_matrix.events.get()
                    if event:
                        row, col = get_coords(event.key_number, len(self.cols))
                        key = self.layer.primary_keys[row][col]
                        print(key.key_names)
                        (key.press if event.pressed else key.release)()

                    device.readinto(self.curr_bitmap, end=len(self.rows))

                    for (row, col), pressed in diff_bitmaps(
                        self.last_bitmap, self.curr_bitmap
                    ):
                        key = self.layer.secondary_keys[row][col]
                        print(key.key_names)
                        (key.press if pressed else key.release)()
                    self.last_bitmap[:] = self.curr_bitmap
                    self.change_layer(device)
                    self.watchdog.feed()

    async def run_as_secondary(self) -> None:
        with I2CTarget(  # type: ignore
            self.i2c_scl_pin, self.i2c_sda_pin, (self.i2c_device_id,)
        ) as device:
            self.neopixel = I2C_SET
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
                                message = request.read(n=3, ack=True)
                                self.neopixel = tuple(message)
                            elif request.is_restart:
                                pass
                            else:
                                request.write(to_bytes(self.matrix_buffer))
                        self.watchdog.feed()

    def change_layer(self, device: I2CDevice):
        if self._prev_layer_index != self.config.layer_index:
            self._prev_layer_index = self.config.layer_index
            if self.primary:
                self.neopixel = self.layer.color
                device.write(b"\x00\x00" + bytes(self.layer.color))
