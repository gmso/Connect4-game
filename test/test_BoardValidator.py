import src.Board as Board
import src.Column as Column
import src.BoardValidator as BoardValidator

def make_column(column_list):
    col = Column.Column()
    for x in range(len(column_list)):
        if column_list[x] == "RED":
            col.cells[x].make_red()
        if column_list[x] == "YELLOW":
            col.cells[x].make_yellow()
    return col

def make_board_won_with_column():
    board = Board.Board()
    board.columns[0] = make_column(["RED","RED","YELLOW","RED","",""])
    board.columns[1] = make_column(["YELLOW","RED","YELLOW","RED","",""])
    board.columns[2] = make_column(["YELLOW","YELLOW","YELLOW","RED","",""])
    board.columns[3] = make_column(["RED","YELLOW","YELLOW","RED","RED","RED"])
    board.columns[4] = make_column(["RED","RED","YELLOW","RED","",""])
    board.columns[5] = make_column(["RED","RED","RED","RED","",""])
    return board

def test_game_won_with_column():
    board = make_board_won_with_column()
    validator = BoardValidator.BoardValidator()
    for x in range(len(board.columns)):
        assert(validator.column_has_4_consecutive_yellows(board.columns[x]) == False)

    reds = board.columns[5].indexes_rows_red()
    assert(validator.column_has_4_consecutive_checkers(reds))

    assert(validator.column_has_4_consecutive_reds(board.columns[0]) == False)
    assert(validator.column_has_4_consecutive_reds(board.columns[1]) == False)
    assert(validator.column_has_4_consecutive_reds(board.columns[2]) == False)
    assert(validator.column_has_4_consecutive_reds(board.columns[3]) == False)
    assert(validator.column_has_4_consecutive_reds(board.columns[4]) == False)
    assert(validator.column_has_4_consecutive_reds(board.columns[5]) == True)

