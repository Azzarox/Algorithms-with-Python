n = 8
matrix = [["-" for _ in range(n)] for _ in range(n)]


def print_matrix(matrix):
    # each row is a list
    for row in matrix:
        print(" ".join(row))
    print()


# need only the row
# we place queens on each row
# when 1 queen is placed on a row it goes to the next row
def can_place_queen(row, col, rows_set, cols_set, left_diagonal_set, right_diagonal_set):
    if row in rows_set:
        return False

    if col in cols_set:
        return False

    if (row - col) in left_diagonal_set:
        return False

    if (row + col) in right_diagonal_set:
        return False

    return True

def set_queen(row, col, matrix, rows_set, cols_set, left_diagonal_set, right_diagonal_set):
    matrix[row][col] = '*'
    rows_set.add(row)
    cols_set.add(col)
    left_diagonal_set.add(row - col)
    right_diagonal_set.add(row + col)


def remove_queen(row, col, matrix, rows_set, cols_set, left_diagonal_set, right_diagonal_set):
    matrix[row][col] = "-"
    rows_set.remove(row)
    cols_set.remove(col)
    left_diagonal_set.remove(row - col)
    right_diagonal_set.remove(row + col)


def place_queens(row, matrix, rows_set, cols_set, left_diagonal_set, right_diagonal_set):
    # the recursion end when it hits the last row
    if row == 8:
        print_matrix(matrix)
        return

        # iterates over all cols
    for col in range(n):
        if can_place_queen(row, col, rows_set, cols_set, left_diagonal_set, right_diagonal_set):
            set_queen(row, col, matrix, rows_set, cols_set, left_diagonal_set, right_diagonal_set)

            place_queens(row + 1, matrix, rows_set, cols_set, left_diagonal_set, right_diagonal_set)

            remove_queen(row, col, matrix, rows_set, cols_set, left_diagonal_set, right_diagonal_set)


place_queens(0, matrix, set(), set(), set(), set())
