from src.Column import Column

class Board():
    columns_total = 7
    columns = [Column() for c in range(columns_total)]