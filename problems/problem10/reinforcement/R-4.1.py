def max(sequence, index=0, current_max=None):
    if index >= len(sequence):
        return current_max
    if current_max is None or sequence[index] > current_max:
        current_max = sequence[index]

    return max(sequence, index + 1, current_max)


print(max([5, 2, 1, 5, 3, 6, 8, 1]))

# runtime is O(n)
# space is O(n)