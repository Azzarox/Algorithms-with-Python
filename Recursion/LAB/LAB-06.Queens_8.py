n = 8
matrix = [["-" for _ in range(n)] for _ in range(n)]


# board = []
# [board.append(['-'] * n) for _ in range(n)]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))
    print()


def can_place_queen(row, col, rows, cols, left_diag, right_diag):
    if row in rows:
        return False

    if col in cols:
        return False

    if (row + col) in right_diag:
        return False

    if (row - col) in left_diag:
        return False

    return True


def set_queen(r, c, matrix, rows, cols, left_diag, right_diag):
    matrix[r][c] = "*"

    rows.add(r)
    cols.add(c)
    left_diag.add(r - c)
    right_diag.add(r + c)


def remove_queen(r, c, matrix, rows, cols, left_diag, right_diag):
    matrix[r][c] = "-"

    rows.remove(r)
    cols.remove(c)
    left_diag.remove(r - c)
    right_diag.remove(r + c)


def put_queens(row, matrix, rows, cols, left_diag, right_diag):
    if row == 8:
        print_matrix(matrix)
        return

    for col in range(8):
        if can_place_queen(row, col, rows, cols, left_diag, right_diag):
            set_queen(row, col, matrix, rows, cols, left_diag, right_diag)  # pre action
            put_queens(row + 1, matrix, rows, cols, left_diag, right_diag)  # recursive call
            remove_queen(row, col, matrix, rows, cols, left_diag, right_diag)  # post action


put_queens(0, matrix, set(), set(), set(), set())
