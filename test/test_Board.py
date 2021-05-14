import src.Board as Board

def test_Column():
    col = Board.Column()
    assert(col.rows_total == 6)
    assert(len(col.cells) == col.rows_total)

def test_Board():
    board = Board.Board()
    assert(board.columns_total == 7)
    assert(len(board.columns) == board.columns_total)