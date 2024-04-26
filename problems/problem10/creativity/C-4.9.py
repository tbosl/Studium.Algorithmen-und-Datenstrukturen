def min_and_max(sequence, current_min=None, current_max=None, index=0):
    if index == len(sequence):
        return current_min, current_max
    item = sequence[index]
    if current_min is None or current_min > item:
        current_min = item
    if current_max is None or current_max < item:
        current_max = item
    return min_and_max(sequence, current_min, current_max, index + 1)


print(min_and_max([4, 2, 1, 5, 3]))
