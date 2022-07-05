cols = int(input())
rows = int(input())

# labyrinth = [[input() for _ in range(rows)]] # matrix with list comprehension

labyrinth = []
for _ in range(rows):
    labyrinth.append(list(input()))

# directions = dict({
#     "R": (0, +1),
#     "L": (0, -1),
#     "U": (+1, 0),
#     "D": (-1, 0),
# })


# direction_keys = list(directions.keys())


def find_all_paths(idx_row, idx_col, direction, matrix, path):
    if idx_row < 0 or idx_col < 0 or idx_col >= len(matrix[0]) or idx_row >= len(matrix):
        return

    if matrix[idx_row][idx_col] == "*":
        return

    if matrix[idx_row][idx_col] == 'v':
        # marks for visited, to reduce going back through already visited
        return

    path.append(direction)

    if matrix[idx_row][idx_col] == "e":
        print("".join(path))
    else:
        matrix[idx_row][idx_col] = 'v'  # first marks and then calls the recursion


        find_all_paths(idx_row, idx_col + 1, "R", matrix, path)
        find_all_paths(idx_row, idx_col - 1, "L", matrix, path)
        find_all_paths(idx_row - 1, idx_col, "U", matrix, path)
        find_all_paths(idx_row + 1, idx_col, "D", matrix, path)

        matrix[idx_row][idx_col] = '-'
    # post action -> removing the last path (r,d,u,d) and unmarking the cells

    path.pop()


find_all_paths(0, 0, "", labyrinth, [])
