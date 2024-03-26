from random import randint


# ns = [n for n in range(5, 105, 5)]
# for n in ns:
#     birth_dates = [Random().randint(1, 365) for i in range(n)]
#     print(birth_dates)
#     checked = []
#     matches = 0
#     for date in birth_dates:
#         if date not in checked:
#             checked.append(date)
#         else:
#             matches += 1
#
#     print((matches / n) * 100)


def has_duplicates(birthdays):
    for i in range(len(birthdays)):
        for j in range(i + 1, len(birthdays)):
            if i == j:
                continue
            if birthdays[i] == birthdays[j]:
                return True
    return False


def birthday_paradox(n, num_simulation):
    duplicates = 0
    for i in range(num_simulation):
        birthdays = []
        for j in range(n):
            birthdays.append(randint(1, 365))
        duplicates += has_duplicates(birthdays)
    return duplicates / num_simulation


print(birthday_paradox(23, 1000))
