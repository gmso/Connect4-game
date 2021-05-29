from src.PlayerInput import PlayerInput


def simulate_key_press(key):

    input = PlayerInput()
    key_not_detected_at_first = input.key_press_detected
    key_detected_after, detected_key = input.wait_for_user_input(key)

    return (key_not_detected_at_first, key_detected_after, detected_key)
