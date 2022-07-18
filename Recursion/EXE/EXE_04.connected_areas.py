class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    matrix.append(list(input()))


def connected_areas(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0

    if matrix[row][col] != "-":  # if is V or * both ways its not viable path
        return 0

    matrix[row][col] = "v"

    result = 1
    result += connected_areas(row + 1, col, matrix)
    result += connected_areas(row - 1, col, matrix)
    result += connected_areas(row, col + 1, matrix)
    result += connected_areas(row, col - 1, matrix)

    return result
    # print_matrix(matrix)


areas = []
for row in range(rows):
    for col in range(cols):
        size = connected_areas(row, col, matrix)
        if size == 0:
            continue
        areas.append(Area(row, col, size))
        # areas.append((row,col,size))

print(f'Total areas found: {len(areas)}')
for idx, area in enumerate(sorted(areas, key=lambda x: x.size, reverse=True)):
    print(f'Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}')
