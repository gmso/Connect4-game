import utility_MakeBoards as BoardMaker
import src.BoardValidatorRows as BoardValidatorRows

def test_game_won_with_column_of_reds():
    board = BoardMaker.make_board_won_with_row_of_reds()
    validator = BoardValidatorRows.BoardValidatorRows()

    assert(validator.connected_4_in_row(board.columns) == True)

def test_game_won_with_column_of_yellows():
    board = BoardMaker.make_board_won_with_row_of_yellows()
    validator = BoardValidatorRows.BoardValidatorRows()

    assert(validator.connected_4_in_row(board.columns) == True)
