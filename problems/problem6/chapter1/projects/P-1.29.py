import math
import random

letters = ['c', 'a', 't', 'd', 'o', 'g']
printed = []
while len(printed) < math.factorial(len(letters)):
    random.shuffle(letters)
    word = ''.join(letters)
    if word not in printed:
        print(word)
        printed.append(word)
