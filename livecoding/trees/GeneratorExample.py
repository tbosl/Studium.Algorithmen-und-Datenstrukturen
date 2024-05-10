for i in range(10):  # [0, 1, 2, 3, ...] -> all generated step-by-step by the generator
    pass


# took forever in for large sets (tuples generated right away)

def firstn(n):
    num = 0
    while num <= n:
        yield num
        num += 1


for i in firstn(10):
    print(i)

i = iter(firstn(10))
print(next(i))
print(next(i))
# l = list(i) --> creates a list from all elements -> next(i) until i has no more next
