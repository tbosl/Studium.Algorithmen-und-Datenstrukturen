def bubble_sort(data):
    n = len(data)
    for i in range(n):
        unchanged = True
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j + 1]
                data[j + 1] = data[j]
                data[j] = temp
                unchanged = False

            if unchanged:
                return data


d = [2, 1, 5, 4, 7, 9]
print(bubble_sort(d))
d = [1, 2, 3, 4, 5]
print(bubble_sort(d))