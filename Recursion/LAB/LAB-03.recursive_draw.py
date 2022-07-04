number = int(input())


# It starts with draw_figure and going downwards ( from 5 to 1 for example )
# When hits 1 it prints the last row of figure and then calls the next function
# Which starts from the last number (which was 1) and goes upwards toward 5

def draw(initial_value_n):

    def draw_figure(max_n):
        if max_n == 1:
            print("*" * max_n)
            return draw_figure_hash(1, initial_value_n)
        print("*" * max_n)
        return draw_figure(max_n - 1)

    def draw_figure_hash(n, max_n):
        if n == max_n:
            print('#' * max_n)
            return
        print("#" * n)
        return draw_figure_hash(n + 1, max_n)

    draw_figure(initial_value_n)

draw(number)
