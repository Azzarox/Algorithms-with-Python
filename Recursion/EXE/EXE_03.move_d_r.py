# rows = int(input())
# cols = int(input())
# #
# matrix = [["-" for _ in range(cols)] for _ in range(rows)]
#
#
# # print(matrix)
# # def print_matrix(matrix):
# #     for row in matrix:
# #         print(' '.join(row))
#
#
# end_row_index = rows - 1
# end_cols_index = cols - 1
# matrix[end_row_index][end_cols_index] = 'e'
#
#
# solutions = []
# def move(row, col, matrix):
#     if row >= len(matrix) or col >= len(matrix[0]):
#         return
#
#     if matrix[row][col] == "v":
#         return
#
#     if matrix[row][col] == 'e':
#         solutions.append(matrix)
#
#         # print_matrix(matrix)
#         # print()
#         return
#
#     matrix[row][col] = "v"
#
#     move(row, col + 1, matrix)
#     move(row + 1, col, matrix)
#
#     matrix[row][col] = '-'
#
#     return len(solutions)
#
#
# print(move(0, 0, matrix))


# lector solution

rows = int(input())
cols = int(input())


def count_all_paths(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0

    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0
    result += count_all_paths(row + 1, col, rows, cols)  # because returns 1 when viable path
    result += count_all_paths(row, col + 1, rows, cols)  # because returns 1 when viable path

    return result


print(count_all_paths(0, 0, rows, cols))
