rows = int(input())
cols = int(input())
#
matrix = [["-" for _ in range(cols)] for _ in range(rows)]


# print(matrix)
# def print_matrix(matrix):
#     for row in matrix:
#         print(' '.join(row))


end_row_index = rows - 1
end_cols_index = cols - 1
matrix[end_row_index][end_cols_index] = 'e'


solutions = []
def move(row, col, matrix):
    if row >= len(matrix) or col >= len(matrix[0]):
        return

    if matrix[row][col] == "v":
        return

    if matrix[row][col] == 'e':
        solutions.append(matrix)

        # print_matrix(matrix)
        # print()
        return

    matrix[row][col] = "v"

    move(row, col + 1, matrix)
    move(row + 1, col, matrix)

    matrix[row][col] = '-'

    return len(solutions)


print(move(0, 0, matrix))
