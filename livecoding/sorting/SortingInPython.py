from operator import itemgetter

data = [85, 24, 63, 45, 17, 31, 96, 50]
print(sorted(data))

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(data, key=itemgetter(1)))  # use index 1 (the integer) within the tuple
# -> sort based on the integer
print(sorted(data, key=itemgetter(1), reverse=True))  # use index 1 (the integer) within the tuple
# -> sort based on the integer but reversed

print(sorted(data, key=itemgetter(0)))  # use index 0 (the string) within the tuple
# -> sort based on the string
print(sorted(data, key=itemgetter(0), reverse=True))  # use index 0 (the string) within the tuple
# -> sort based on the string but reversed
