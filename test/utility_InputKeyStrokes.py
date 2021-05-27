import threading
import time
from pynput import keyboard
from src.PlayerInput import PlayerInput


def press_key_repeatedly(key):
    """Press key, wating 10ms before press"""

    controller = keyboard.Controller()

    time.sleep(0.01)
    controller.press(key)


def press_key_scenario(key):
    input = PlayerInput()

    simulated_player_input_thread = threading.Thread(
        target=press_key_repeatedly, args=(key,))

    key_not_detected_at_first = input.key_press_detected

    simulated_player_input_thread.start()
    key_detected_after, detected_key = input.wait_for_user_input()
    simulated_player_input_thread.join()

    return (key_not_detected_at_first, key_detected_after, detected_key)


def simulate_key_press(key):
    input = PlayerInput()
    key_not_detected_at_first = input.key_press_detected
    key_detected_after, detected_key = input.wait_for_user_input(key)
    return (key_not_detected_at_first, key_detected_after, detected_key)
