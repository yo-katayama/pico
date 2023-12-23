import board
import digitalio
import time

def blink_led_for_seconds(seconds):
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT

    led.value = True
    print(f"*** Activate LED {seconds} seconds ON!! ***")
    time.sleep(seconds)
    led.value = False

def blink_led():
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    led.value = True

def turn_off_led():
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    led.value = False
