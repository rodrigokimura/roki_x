import time

import board
import busio
import digitalio

import supervisor
import neopixel
from adafruit_bus_device.i2c_device import I2CDevice
from i2ctarget import I2CTarget
from utils import parse_color

I2C_DEVICE_ID = 0x08


class RokiX:
    def __init__(self) -> None:
        self.pixels = neopixel.NeoPixel(board.GP23, 1)  # type: ignore
        self.pixels.brightness = 0.5

        self.i2c_scl_pin = board.GP1  # type: ignore
        self.i2c_sda_pin = board.GP0  # type: ignore
        self.buffer = bytearray(3)

    @property
    def primary(self):
        return supervisor.runtime.usb_connected

    def get_device(self):
        with busio.I2C(scl=self.i2c_scl_pin, sda=self.i2c_sda_pin) as i2c:
            with I2CDevice(i2c, I2C_DEVICE_ID, True) as device:
                yield device

    def run(self):
        self.pixels[0] = parse_color("#ffffff")
        if self.primary:
            for i in range(10):
                try:
                    with busio.I2C(scl=self.i2c_scl_pin, sda=self.i2c_sda_pin) as i2c:
                        with I2CDevice(i2c, I2C_DEVICE_ID, False) as device:
                            self.pixels[0] = parse_color("#ffff00")
                            time.sleep(1)
                            while True:
                                device.readinto(self.buffer)
                                if self.buffer:
                                    self.pixels[0] = parse_color("#00ff00")
                                else:
                                    self.pixels[0] = parse_color("#ff0000")
                                print(self.buffer)
                except Exception as e:
                    print(e)
                    time.sleep(1)
                    self.pixels[0] = parse_color("#ff0000")
        else:
            with I2CTarget(
                self.i2c_scl_pin, self.i2c_sda_pin, (I2C_DEVICE_ID,)
            ) as device:
                self.pixels[0] = parse_color("#00ffff")
                time.sleep(1)
                while True:
                    r = device.request()
                    if not r:
                        continue
                    with r:
                        if r.address == I2C_DEVICE_ID:
                            if not r.is_read:
                                r.read(1)
                            elif r.is_restart:
                                r.write(bytes([1, 2, 3]))
                            else:
                                self.pixels[0] = parse_color("#0000ff")
                                r.write(bytes([4, 5, 6]))


if __name__ == "__main__":
    time.sleep(1)
    RokiX().run()
