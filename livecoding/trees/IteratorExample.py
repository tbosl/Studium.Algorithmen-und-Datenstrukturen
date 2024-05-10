data = [4, 3, 2, 10, 50, 9]
for i in data:
    print(i)

i1 = iter(data)
i2 = iter(data)
print(next(i1))
print(next(i1))
print(next(i2))
