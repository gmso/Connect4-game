from unittest.mock import patch

def simulate_key_press(key):

    patcher = patch('pynput.keyboard.backend(package)', lambda x: x)
    patcher.start()

    from src.PlayerInput import PlayerInput

    input = PlayerInput()
    key_not_detected_at_first = input.key_press_detected
    key_detected_after, detected_key = input.wait_for_user_input(key)

    patcher.stop()
    return (key_not_detected_at_first, key_detected_after, detected_key)
