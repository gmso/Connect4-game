class BoardValidator():
    def game_won(self,columns):
        pass

    def connected_4_in_column(self,columns):
        for col in columns:
            if self.column_has_4_consecutive_reds(col):
                return True
            if self.column_has_4_consecutive_yellows(col):
                return True

    def column_has_4_consecutive_reds(self,col):
        reds = col.indexes_rows_red()
        return self.column_has_4_consecutive_checkers(reds)

    def column_has_4_consecutive_yellows(self,col):
        yellows = col.indexes_rows_yellow()
        return self.column_has_4_consecutive_checkers(yellows)

    def column_has_4_consecutive_checkers(self,reduction):
        if len(reduction) >= 4:
            diffs = [(reduction[x+1] - reduction[x]) for x in range(len(reduction)-1)]
            for x in range(len(diffs)-2):
                if [diffs[x],diffs[x+1],diffs[x+2]] == [1,1,1]:
                    return True
        return False

    def connected_4_in_row(self):
        pass

    def connected_4_in_diagonal(self):
        pass
