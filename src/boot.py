import supervisor  # type: ignore

if __name__ == "__main__":
    supervisor.set_usb_identification(manufacturer="RokiX", product="roki_x")
