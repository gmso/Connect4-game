import src.BoardValidatorColumns as BVC
import src.BoardValidatorRows as BVR
import src.BoardValidatorDiagonals as BVD


class BoardValidator():
    def __init__(self) -> None:
        self.validator_columns = BVC.BoardValidatorColumns()
        self.validator_rows = BVR.BoardValidatorRows()
        self.validator_diagonals = BVD.BoardValidatorDiagonals()

    def game_won(self, columns):
        return (
            self.validator_columns.connected_4_in_column(columns) or
            self.validator_rows.connected_4_in_row(columns) or
            self.validator_diagonals.connected_4_in_diagonal(columns)
            )
