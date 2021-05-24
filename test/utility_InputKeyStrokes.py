import time
from pynput import keyboard


def press_key_repeatedly(key):
    """Press key, wating 10ms before press"""

    controller = keyboard.Controller()

    time.sleep(0.01)
    controller.press(key)
