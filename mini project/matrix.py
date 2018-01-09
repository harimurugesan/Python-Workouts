class Matrix:
    def __init__(self, rows, columns, default_character='x'):
        self.rows = rows
        self.columns = columns
        self.grid = [[default_character] * columns for _ in range(rows)]

    def print_matrix(self):
        for row in self.grid:
            print(''.join(row))

    def update_character_in_matrix(self, row_number, column_number, new_character):
        if 0 <= row_number < self.rows:

            if 0 <= column_number < self.columns:
                self.grid[row_number][column_number] = new_character
                return
        raise IndexError("index error .index out of bounds")



