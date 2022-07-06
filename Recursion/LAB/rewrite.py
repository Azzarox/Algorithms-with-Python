r = int(input())
c = int(input())
lab = [[input()] for _ in range(r)]


def find_all_path(idx_r, idx_c, matrix, direction, path):
    if idx_r < 0 or idx_c < 0 or idx_c >= len(matrix[0]) or idx_r >= len(matrix):
        return

    if matrix[idx_r][idx_c] == '*':
        return

    if matrix[idx_r][idx_c] == 'v':
        return

    path.append(direction)

    if matrix[idx_r][idx_c] == "e":
        print("".join(path))
    else:
        matrix[idx_r][idx_c] = 'v'

        find_all_path(idx_r, idx_c + 1, matrix, "R", path)
        find_all_path(idx_r, idx_c - 1, matrix, "L", path)
        find_all_path(idx_r + 1, idx_c, matrix, "U", path)
        find_all_path(idx_r - 1, idx_c, matrix, "D", path)

        matrix[idx_r][idx_c] = '-'

    path.pop()


find_all_path(0, 0, lab, "", [])
