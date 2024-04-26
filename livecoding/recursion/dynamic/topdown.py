memory = {0: 0, 1: 1}


def fib(n):
    if n not in memory:
        memory[n] = fib(n - 1) + fib(n - 2)
    return memory[n]


print(fib(999))
for k in memory:
    print(str(k) + ": " + str(memory[k]))
