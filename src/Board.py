from src.Column import Column
from src.BoardValidator import BoardValidator

class Board():
    columns_total = 7

    def __init__(self) -> None:
        self.columns = [Column() for c in range(self.columns_total)]
        self.validator = BoardValidator()
    