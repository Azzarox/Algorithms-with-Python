n = int(input("Enter number of queens: "))
matrix = [["-" for _ in range(n)] for _ in range(n)]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))
    print()


def can_place_queen(row, col, rows, cols, left, right):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in left:
        return False
    if (row + col) in right:
        return False

    return True


def set_queen(row, col, matrix, rows, cols, left, right):
    matrix[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left.add((row - col))
    right.add((row + col))


def remove_queen(row, col, matrix, rows, cols, left, right):
    matrix[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left.remove((row - col))
    right.remove((row + col))


def place_queens(row, matrix, rows, cols, left, right):
    if row == n:
        print(f'-- Solution --')
        print_matrix(matrix)
        return

    for col in range(n):
        if can_place_queen(row, col, rows, cols, left, right):
            set_queen(row, col, matrix, rows, cols, left, right)
            place_queens(row + 1, matrix, rows, cols, left, right)
            remove_queen(row, col, matrix, rows, cols, left, right)


place_queens(0, matrix, set(), set(), set(), set())
