def sum_of_squares_of_odd_numbers_until_n(n):
    return sum((k * k for k in range(1, n) if k % 2 == 1))


print(sum_of_squares_of_odd_numbers_until_n(5))
print(sum_of_squares_of_odd_numbers_until_n(10))
print(sum_of_squares_of_odd_numbers_until_n(100))
print(sum_of_squares_of_odd_numbers_until_n(-1))
