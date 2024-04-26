def linear_search(data, target):
    for val in data:
        if val == target:
            return True
    return False


print(linear_search([3, 2, 1, 6, 5], 3))
print(linear_search([3, 2, 1, 6, 5], 5))
print(linear_search([3, 2, 1, 6, 5], 10))
