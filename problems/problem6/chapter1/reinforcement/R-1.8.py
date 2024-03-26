def get_by_index(d, index):
    return d[index]


data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
k = -7
print(get_by_index(data, k))
print(get_by_index(data, len(data) + k))
