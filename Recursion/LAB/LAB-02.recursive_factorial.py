number = int(input())


def recursive(number):
    if number == 1:
        return 1
    return number * recursive(number - 1)


print(recursive(number))
