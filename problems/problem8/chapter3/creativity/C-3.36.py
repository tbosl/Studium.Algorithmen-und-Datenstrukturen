import random


def find_ten_largest_elements(numbers):
    largest = []
    for n in numbers:
        if len(largest) < 10:
            largest.append(n)
            continue
        smallest_index = 0
        for i in range(10):
            if largest[i] < largest[smallest_index]:
                smallest_index = i
        if largest[smallest_index] < n:
            largest[smallest_index] = n
    largest.sort()
    return largest  # --> complexity is O(n)


print(find_ten_largest_elements([n for n in range(20)]))
r = random.Random()
l = [r.randint(0, 20) for n in range(20)]
print(find_ten_largest_elements(l))
l.sort()
print(l)
