import src.constants as const 
from src.Column import Column
from src.BoardValidator import BoardValidator


class Board():
    columns_total = const.BOARD_TOTAL_COLUMNS

    def __init__(self) -> None:
        self.columns = [Column() for c in range(self.columns_total)]
        self.validator = BoardValidator()
