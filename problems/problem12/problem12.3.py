def flatten(tree):
    for subtree in tree:
        if isinstance(subtree, list):
            yield from flatten(subtree)
        else:
            yield subtree


data = [[1], [2, 3], [4, [5, 6, [7, 8, [9, [10, 11, 12]]]]]]
for i in flatten(data):
    print(i)
