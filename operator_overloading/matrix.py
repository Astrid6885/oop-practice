"""Problem 7 - Matrix: overload * to multiply two matrices."""


class Matrix:
    def __init__(self, rows):
        # rows is a list of lists, e.g. [[1, 2], [3, 4]]
        self.rows = rows
        self.n_rows = len(rows)
        self.n_cols = len(rows[0])

    def __mul__(self, other):
        # We can only multiply (n x m) by (m x p)
        if self.n_cols != other.n_rows:
            raise ValueError("Cannot multiply: number of columns of the first matrix "
                             "must equal number of rows of the second matrix.")

        result = []
        for i in range(self.n_rows):
            new_row = []
            for j in range(other.n_cols):
                # Cell (i, j) = sum of row i of self times column j of other
                total = 0
                for k in range(self.n_cols):
                    total += self.rows[i][k] * other.rows[k][j]
                new_row.append(total)
            result.append(new_row)

        return Matrix(result)

    def __eq__(self, other):
        return self.rows == other.rows

    def __str__(self):
        return "\n".join(str(row) for row in self.rows)


if __name__ == "__main__":
    a = Matrix([[1, 2],
                [3, 4]])
    b = Matrix([[5, 6],
                [7, 8]])
    print("A * B =")
    print(a * b)  # [[19, 22], [43, 50]]
