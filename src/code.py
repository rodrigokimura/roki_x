import asyncio

from firmware.kb import RokiX

I2C_DEVICE_ID = 0x08

if __name__ == "__main__":  # pragma: no cover
    asyncio.run(RokiX(I2C_DEVICE_ID).run())
