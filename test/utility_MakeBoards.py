import src.Board as Board
import src.Column as Column

def make_column(column_list):
    col = Column.Column()
    for x in range(len(column_list)):
        if column_list[x] == "RED":
            col.cells[x].make_red()
        if column_list[x] == "YELLOW":
            col.cells[x].make_yellow()
    return col

def make_board_won_with_row_of_reds():
    board = Board.Board()
    board.columns[0] = make_column(["RED","RED","YELLOW","","",""])
    board.columns[1] = make_column(["YELLOW","RED","RED","RED","",""])
    board.columns[2] = make_column(["YELLOW","YELLOW","RED","","",""])
    board.columns[3] = make_column(["RED","YELLOW","RED","","",""])
    board.columns[4] = make_column(["RED","YELLOW","RED","","",""])
    board.columns[5] = make_column(["RED","RED","YELLOW","RED","",""])
    return board

def make_board_won_with_row_of_yellows():
    board = Board.Board()
    board.columns[0] = make_column(["RED","RED","YELLOW","RED","",""])
    board.columns[1] = make_column(["YELLOW","RED","RED","RED","",""])
    board.columns[2] = make_column(["YELLOW","YELLOW","YELLOW","","",""])
    board.columns[3] = make_column(["RED","YELLOW","YELLOW","","",""])
    board.columns[4] = make_column(["RED","RED","YELLOW","RED","",""])
    board.columns[5] = make_column(["RED","RED","YELLOW","RED","",""])
    return board

def make_board_won_with_column_of_reds():
    board = Board.Board()
    board.columns[0] = make_column(["RED","RED","YELLOW","RED","",""])
    board.columns[1] = make_column(["YELLOW","RED","YELLOW","RED","",""])
    board.columns[2] = make_column(["YELLOW","YELLOW","YELLOW","RED","",""])
    board.columns[3] = make_column(["RED","YELLOW","YELLOW","RED","RED","RED"])
    board.columns[4] = make_column(["RED","RED","YELLOW","RED","",""])
    board.columns[5] = make_column(["RED","RED","RED","RED","",""])
    return board


def make_board_won_with_column_of_yellows():
    board = Board.Board()
    board.columns[0] = make_column(["RED","RED","YELLOW","RED","",""])
    board.columns[1] = make_column(["YELLOW","RED","YELLOW","RED","",""])
    board.columns[2] = make_column(["YELLOW","YELLOW","YELLOW","RED","",""])
    board.columns[3] = make_column(["RED","YELLOW","YELLOW","YELLOW","YELLOW",""])
    board.columns[4] = make_column(["RED","RED","YELLOW","RED","",""])
    board.columns[5] = make_column(["RED","RED","RED","","",""])
    return board

