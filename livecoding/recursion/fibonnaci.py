from functools import lru_cache


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


@lru_cache()  # memoizing
def fib_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_2(n - 1) + fib_2(n - 2)


print(fib(10))
print(fib_2(100))
