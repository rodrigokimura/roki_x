import os

import storage  # type: ignore
import supervisor  # type: ignore
import usb_cdc  # type: ignore


def rename(new_name: str):
    storage.remount("/", readonly=False)
    m = storage.getmount("/")
    m.label = new_name
    storage.remount("/", readonly=True)


if __name__ == "__main__":
    if not os.getenv("ENABLE_SERIAL", True):
        usb_cdc.disable()
    supervisor.set_usb_identification(manufacturer="RokiX", product="roki_x")
    rename("ROKI_X")
