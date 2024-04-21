def search_binary(data, target, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(data) - 1
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return search_binary(data, target, low, mid - 1)
        else:
            return search_binary(data, target, mid + 1, high)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = [i for i in range(10, 0, -1)]
print(search_binary(a, 9))
# print(b)
# print(search_binary(b, 9))
c = [i for i in range(10_000_000)]
#print(c)
print(search_binary(c, 10))
