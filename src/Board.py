from src.Cell import Cell 

class Column():
    rows_total = 6
    cells = [Cell() for r in range(rows_total)]


class Board():
    columns_total = 7
    columns = [Column() for c in range(columns_total)]