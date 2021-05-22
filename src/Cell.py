import src.constants as const 


class Cell():
    def __init__(self) -> None:
        self.current_state = const.CellState.EMPTY

    def is_empty(self):
        return (self.current_state == const.CellState.EMPTY)

    def is_red(self):
        return (self.current_state == const.CellState.RED)

    def is_yellow(self):
        return (self.current_state == const.CellState.YELLOW)

    def make_red(self):
        self.current_state = const.CellState.RED

    def make_yellow(self):
        self.current_state = const.CellState.YELLOW
