from enum import Enum

class State(Enum):
    EMPTY = 0
    RED = 1
    YELLOW = 2

class Cell():
    def __init__(self) -> None:
        self.current_state = State.EMPTY

    def is_empty(self):
        return (self.current_state == State.EMPTY)

    def is_red(self):
        return (self.current_state == State.RED)

    def is_yellow(self):
        return (self.current_state == State.YELLOW)

    def make_red(self):
        self.current_state = State.RED

    def make_yellow(self):
        self.current_state = State.YELLOW