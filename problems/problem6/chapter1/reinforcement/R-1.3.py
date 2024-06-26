# correct
def minmax(data):
    if not data:
        print("Empty data provided")
        return
    minimum = maximum = data[0]
    for d in data[1:]:
        if d < minimum:
            minimum = d
        elif maximum < d:
            maximum = d
    return minimum, maximum


print(minmax((5, 7, -20, 10, 21, -5, 2)))
print(minmax(()))
