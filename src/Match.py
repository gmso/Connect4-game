import src.constants as const
from src.Board import Board


class Match():
    def __init__(self, first_player=const.PlayerTurn.RED) -> None:
        self.board = Board()
        self.column_selected = 0
        self.state = const.MatchState.PLAYING
        self.player_turn = first_player

    def add_checker(self):
        if self.player_turn == const.PlayerTurn.RED:
            self.board.add_checker_red(self.column_selected)
        else:
            self.board.add_checker_yellow(self.column_selected)

        if self.board.is_game_won():
            self.state = (
                const.MatchState.RED_WON
                if self.player_turn == const.PlayerTurn.RED else
                const.MatchState.YELLOW_WON)
        else:
            self._toggle_player()

    def column_next(self):
        increment = 1
        self._column_change(increment)

    def column_previous(self):
        increment = -1
        self._column_change(increment)

    def is_being_played(self):
        return self.state == const.MatchState.PLAYING

    def _column_change(self, increment):
        self.column_selected += increment

        if self.column_selected == const.BOARD_TOTAL_COLUMNS:
            self.column_selected = 0
        elif self.column_selected < 0:
            self.column_selected = const.BOARD_TOTAL_COLUMNS - 1

        if self.board.columns[self.column_selected].is_full():
            self._column_change(increment)

    def _toggle_player(self):
        self.player_turn = (
                const.PlayerTurn.RED
                if self.player_turn == const.PlayerTurn.YELLOW else
                const.PlayerTurn.YELLOW)
