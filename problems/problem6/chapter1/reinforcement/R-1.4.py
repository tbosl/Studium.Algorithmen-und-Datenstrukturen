def sum_of_squares_until_n(n):
    assert n > 0
    count = 0
    for k in range(1, n):  # add only positive numbers
        count += k * k
    return count


print(sum_of_squares_until_n(5))
print(sum_of_squares_until_n(10))
print(sum_of_squares_until_n(100))
print(sum_of_squares_until_n(-1))
