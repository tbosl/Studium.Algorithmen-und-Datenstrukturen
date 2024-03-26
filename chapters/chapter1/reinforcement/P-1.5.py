def sum_of_squares_until_n(n):
    return sum((k * k for k in range(n)))


print(sum_of_squares_until_n(5))
print(sum_of_squares_until_n(10))
print(sum_of_squares_until_n(100))
print(sum_of_squares_until_n(-1))
