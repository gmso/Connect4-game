import src.constants as const 
from src.Board import Board


class Match():
    def __init__(self, first_player=const.PlayerTurn.RED) -> None:
        self.board = Board()
        self.column_selection = 0
        self.state = const.MatchState.PLAYING
        self.player_turn = first_player

    def column_next(self):
        increment = 1
        self._column_change(increment)

    def column_previous(self):
        increment = -1
        self._column_change(increment)

    def _column_change(self, increment):
        self.column_selection += increment

        if self.column_selection == const.BOARD_TOTAL_COLUMNS:
            self.column_selection = 0
        elif self.column_selection < 0:
            self.column_selection = const.BOARD_TOTAL_COLUMNS - 1

        if self.board.columns[self.column_selection].is_full():
            self._column_change(increment)
