import numpy as np


def change_type(matrix):
    values = list(map(int, matrix.split(' ')))
    return values


def check(matrix):
    if matrix.first_matrix.rows == matrix.second_matrix.rows and matrix.first_matrix.col == matrix.second_matrix.col:
        return True
    else:
        return False


class Matrix:
    def __init__(self, rows=1, col=1, matrix=[1]):
        self.rows = int(rows)
        self.col = int(col)
        self.matrix = np.array(matrix)
        self.matrix = np.reshape(self.matrix, (self.rows, self.col))


class LastMatrix:
    POSSIBLE_ITEMS = ['first_rows', 'first_col', 'first_matrix', 'second_rows', 'second_col', 'second_matrix', ]

    def __init__(self):
        self.first_matrix = Matrix()
        self.second_matrix = Matrix()

    def add_matrix(self, first_rows, first_col, first_matrix, second_rows, second_col, second_matrix):
        first_matrix = change_type(first_matrix)
        second_matrix = change_type(second_matrix)
        self.first_matrix = Matrix(first_rows, first_col, first_matrix)
        self.second_matrix = Matrix(second_rows, second_col, second_matrix)
        return 'Done'

    def amount(self):
        if check(self):
            amount = str(self.first_matrix.matrix + self.second_matrix.matrix)
        else:
            amount = 'Incompatible matrices!'
        return amount

    def difference(self):
        if check(self):
            difference = str(self.first_matrix.matrix - self.second_matrix.matrix)
        else:
            difference = 'Incompatible matrices!'
        return difference

    def multiplication(self):
        if check(self):
            multiplication = str(self.first_matrix.matrix * self.second_matrix.matrix)
        else:
            multiplication = 'Incompatible matrices!'
        return multiplication

