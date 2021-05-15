import src.BoardValidatorColumns as BoardValidatorColumns
import src.BoardValidatorRows as BoardValidatorRows

class BoardValidator():
    def __init__(self) -> None:
        self.validator_columns = BoardValidatorColumns.BoardValidatorColumns()
        self.validator_rows = BoardValidatorRows.BoardValidatorRows()

    def game_won(self,columns):
        return (
            self.validator_columns.connected_4_in_column(columns) or
            self.validator_rows.connected_4_in_column(columns)
            )

    def connected_4_in_diagonal(self):
        pass
