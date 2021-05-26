import threading
from pynput import keyboard
from src.constants import ValidUserInput as UserInput
from src.PlayerInput import PlayerInput
from utility_InputKeyStrokes import press_key_repeatedly as key_repeat


def press_key_scenario(key):
    input = PlayerInput()

    simulated_player_input_thread = threading.Thread(
        target=key_repeat, args=(key,))

    key_not_detected_at_first = input.key_press_detected

    simulated_player_input_thread.start()
    key_detected_after, detected_key = input.wait_for_user_input()
    simulated_player_input_thread.join()

    return (key_not_detected_at_first, key_detected_after, detected_key)


def test_key_press_left():
    key = keyboard.Key.left

    before, after, key_detected = press_key_scenario(key)
    assert not(before)
    assert(after)
    assert(key_detected == UserInput.ARROW_LEFT)


def test_key_press_right():
    key = keyboard.Key.right

    before, after, key_detected = press_key_scenario(key)
    assert not(before)
    assert(after)
    assert(key_detected == UserInput.ARROW_RIGHT)


def test_key_press_enter():
    key = keyboard.Key.enter

    before, after, key_detected = press_key_scenario(key)
    assert not(before)
    assert(after)
    assert(key_detected == UserInput.ENTER)


def test_key_press_r():
    key = "r"

    before, after, key_detected = press_key_scenario(key)
    assert not(before)
    assert(after)
    assert(key_detected == UserInput.KEY_R)


def test_key_press_q():
    key = "q"

    before, after, key_detected = press_key_scenario(key)
    assert not(before)
    assert(after)
    assert(key_detected == UserInput.KEY_Q)
