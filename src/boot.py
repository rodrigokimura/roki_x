# from time import sleep
#
# import board
# import digitalio
#
# led = digitalio.DigitalInOut(board.LED)  # type: ignore
# led.direction = digitalio.Direction.OUTPUT
#
#
# def toggle(led: digitalio.DigitalInOut):
#     led.value = not led.value
#
#
# def fast_blink():
#     for _ in range(6):
#         toggle(led)
#         sleep(0.1)
#
#
# if __name__ == "__main__":
#     fast_blink()
