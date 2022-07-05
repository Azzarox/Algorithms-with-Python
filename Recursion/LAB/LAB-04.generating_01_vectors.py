n = int(input())
vector = [None] * n  # Fills the initial list


def fill_vector(idx, vector):
    if idx >= len(vector):  # when the index has reached the last index or more it prints and finishes
        print(vector)
        return
    for i in range(2):
        # Generating 0 and 1, when the recursion call is done the functions continues in the for loop
        # Until it has finished the combinations
        vector[idx] = i  # sets the number in the list to the i - 0 or 1
        fill_vector(idx + 1, vector)  # calls the function with increased index


fill_vector(0, vector)
