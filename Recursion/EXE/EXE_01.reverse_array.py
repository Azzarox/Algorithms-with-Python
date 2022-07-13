arr = input().split()

reversed_arr = []


def reverse_arr(idx, arr):
    if idx < 0:
        print(" ".join(reversed_arr))
        return
    reversed_arr.append(arr[idx])
    reverse_arr(idx - 1, arr)


reverse_arr(len(arr) - 1, arr)
