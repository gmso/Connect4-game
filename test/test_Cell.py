import src.Cell as Cell

def test_Cell():
    cell = Cell.Cell()
    assert (cell.current_state == Cell.CellState.EMPTY)