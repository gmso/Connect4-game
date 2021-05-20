import utility_MakeBoards as BoardMaker
import src.BoardValidatorColumns as BVC

def test_game_won_with_column_of_reds():
    board = BoardMaker.make_board_won_with_column_of_reds()
    validator = BVC.BoardValidatorColumns()
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

    assert(validator.connected_4_in_column(board.columns) == True)

def test_game_won_with_column_of_yellows():
    board = BoardMaker.make_board_won_with_column_of_yellows()
    validator = BVC.BoardValidatorColumns()
    for x in range(len(board.columns)):
        assert(validator.column_has_4_consecutive_reds(board.columns[x]) == False)

    yellows = board.columns[3].indexes_rows_yellow()
    assert(validator.column_has_4_consecutive_checkers(yellows))

    assert(validator.column_has_4_consecutive_yellows(board.columns[0]) == False)
    assert(validator.column_has_4_consecutive_yellows(board.columns[1]) == False)
    assert(validator.column_has_4_consecutive_yellows(board.columns[2]) == False)
    assert(validator.column_has_4_consecutive_yellows(board.columns[3]) == True)
    assert(validator.column_has_4_consecutive_yellows(board.columns[4]) == False)
    assert(validator.column_has_4_consecutive_yellows(board.columns[5]) == False)

    assert(validator.connected_4_in_column(board.columns) == True)