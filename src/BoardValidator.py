import src.BoardValidatorColumns as BoardValidatorColumns
import src.BoardValidatorRows as BoardValidatorRows
import src.BoardValidatorDiagonals as BoardValidatorDiagonals

class BoardValidator():
    def __init__(self) -> None:
        self.validator_columns = BoardValidatorColumns.BoardValidatorColumns()
        self.validator_rows = BoardValidatorRows.BoardValidatorRows()
        self.validator_diagonals = BoardValidatorDiagonals.BoardValidatorDiagonals()

    def game_won(self,columns):
        return (
            self.validator_columns.connected_4_in_column(columns) or
            self.validator_rows.connected_4_in_column(columns) or
            self.validator_diagonals.connected_4_in_column(columns)
            )