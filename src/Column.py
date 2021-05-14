from src.Cell import Cell 

class Column():
    rows_total = 6
    cells = [Cell() for r in range(rows_total)]

    def add_checker_red(self):
        index = self.get_first_row_empty()
        self.cells[index].make_red()

    def add_checker_yellow(self):
        index = self.get_first_row_empty()
        self.cells[index].make_yellow()

    def get_rows_empty(self):
        return len([c for c in self.cells if c.is_empty()])

    def get_rows_red(self):
        return len([c for c in self.cells if c.is_red()])

    def get_rows_yellow(self):
        return len([c for c in self.cells if c.is_yellow()])

    def get_first_row_empty(self):
        return self.rows_total - self.get_rows_empty()
