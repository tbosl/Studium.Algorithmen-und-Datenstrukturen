def faster_power(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return x * faster_power(x, n / 2) ** 2
    return x * faster_power(x, n // 2) ** 2


print(faster_power(2, 30))
# O(log(n))
