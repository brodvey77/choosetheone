
class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self._matrix = [[value for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        return self._matrix[row][col]

    def set_value(self, row, col, value):
        self._matrix[row][col] = value

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __str__(self):
        return '\n'.join(' '.join(str(el) for el in row) for row in self._matrix)

    def __pos__(self):
        result = Matrix(self.rows, self.cols)
        result._matrix = [row[:] for row in self._matrix]
        return result

    def __neg__(self):
        new_matrix = Matrix(self.rows, self.cols)
        new_matrix._matrix = [[-x for x in row] for row in self._matrix]
        return new_matrix

    def __invert__(self):
        new_matrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.set_value(j, i, self._matrix[i][j])
        return new_matrix

    def __round__(self, ndigits=None):
        new_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                if ndigits is None:
                    new_matrix.set_value(i, j, round(self._matrix[i][j]))
                else:
                    new_matrix.set_value(i, j, round(self._matrix[i][j], ndigits))
        return new_matrix





matrix = Matrix(2, 3, 1)

print(+matrix)
print()
print(-matrix)


class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self._matrix = [[value] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self._matrix[row][col]

    def set_value(self, row, col, value):
        self._matrix[row][col] = value

    def __str__(self):
        string_matrix = [[str(ele) for ele in row] for row in self._matrix]
        return '\n'.join(' '.join(row) for row in string_matrix)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __pos__(self):
        matrix = Matrix(self.rows, self.cols)
        for row in range(matrix.rows):
            for col in range(matrix.cols):
                matrix.set_value(row, col, self.get_value(row, col))
        return matrix

    def __neg__(self):
        matrix = Matrix(self.rows, self.cols)
        for row in range(matrix.rows):
            for col in range(matrix.cols):
                matrix.set_value(row, col, -self.get_value(row, col))
        return matrix

    def __round__(self, n):
        matrix = Matrix(self.rows, self.cols)
        for row in range(matrix.rows):
            for col in range(matrix.cols):
                matrix.set_value(row, col, round(self.get_value(row, col), n))
        return matrix

    def __invert__(self):
        matrix = Matrix(self.cols, self.rows)
        for row in range(self.cols):
            for col in range(self.rows):
                matrix.set_value(row, col, self.get_value(col, row))
        return matrix