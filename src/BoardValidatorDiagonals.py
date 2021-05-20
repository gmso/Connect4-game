class BoardValidatorDiagonals():

    def connected_4_in_diagonal(self, columns):
        reduced_columns_reds = [c.indexes_rows_red() for c in columns]
        reduced_columns_yellows = [c.indexes_rows_yellow() for c in columns]
        return (
            self.board_has_4_diagonal_checkers(reduced_columns_reds) or
            self.board_has_4_diagonal_checkers(reduced_columns_yellows)
            )

    def board_has_4_diagonal_checkers(self, reduced_columns):
        for c in range(len(reduced_columns)-3):
            for r in reduced_columns[c]:
                if ((r+1) in reduced_columns[c+1] and
                        (r+2) in reduced_columns[c+2] and
                        (r+3) in reduced_columns[c+3]):
                    return True
                if r >= 3:
                    if ((r-1) in reduced_columns[c+1] and
                            (r-2) in reduced_columns[c+2] and
                            (r-3) in reduced_columns[c+3]):
                        return True
        return False
