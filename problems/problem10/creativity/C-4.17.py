def is_palindrome(message, index=0):
    if index > len(message) / 2:
        return True
    return message[index] == message[len(message) - index - 1] and is_palindrome(message, index + 1)


print(is_palindrome('abccba'))
print(is_palindrome('test'))
print(is_palindrome('racecar'))
print(is_palindrome('gohangasalamiimalasagnahog'))
