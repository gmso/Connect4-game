import src.Board as Board
import src.Cell as Cell

def test_Board_construction():
    board = Board.Board()
    assert(board.columns_total == 7)
    assert(len(board.columns) == board.columns_total)