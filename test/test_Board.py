import src.Board as Board

def test_Board():
    board = Board.Board()
    assert(board.rows == 6)
    assert(board.columns == 7)