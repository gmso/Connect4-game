from enum import Enum


BOARD_TOTAL_COLUMNS = 7
BOARD_TOTAL_ROWS_PER_COLUMN = 6


class PlayerTurn(Enum):
    RED = 0
    YELLOW = 1


class MatchState(Enum):
    PLAYING = 0
    RED_WON = 1
    YELLOW_WON = 2
    TIE = 3


class CellState(Enum):
    EMPTY = 0
    RED = 1
    YELLOW = 2
