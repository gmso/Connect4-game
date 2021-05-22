import src.constants as const 
import src.Cell as Cell

def test_Cell_construction():
    cell = Cell.Cell()
    assert (cell.current_state == const.CellState.EMPTY)
    assert (cell.is_empty() == True)
    assert (cell.is_red() == False)
    assert (cell.is_yellow() == False)
    
def test_Cell_make_red():
    cell = Cell.Cell()
    cell.make_red()
    assert (cell.is_empty() == False)
    assert (cell.is_red() == True)
    assert (cell.is_yellow() == False)

def test_Cell_make_yellow():
    cell = Cell.Cell()
    cell.make_yellow()
    assert (cell.is_empty() == False)
    assert (cell.is_red() == False)
    assert (cell.is_yellow() == True)
