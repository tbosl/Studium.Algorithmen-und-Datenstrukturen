import math
import time
from random import uniform


class Circle:
    def __init__(self):
        self.radius = 0.5
        self.center_x = 0.5
        self.center_y = 0.5
        self.comparer_runtime = 0

    def within_circle(self, x, y):
        start = time.time()
        distance = (x - self.center_x) ** 2 + (y - self.center_y) ** 2
        self.comparer_runtime += (time.time() - start)
        return distance <= self.radius ** 2


class Square:
    def __init__(self):
        self.side_length = 1
        self.bottom_left = (0, 0)
        self.bottom_right = (1, 0)
        self.upper_right = (1, 1)
        self.upper_left = (0, 1)

    def within_square(self, x, y):
        return self.bottom_left[0] <= x <= self.bottom_right[0] and self.bottom_left[1] <= y <= self.upper_right[1]


def random_spawn():
    return uniform(0, 1), uniform(0, 1)


c = Circle()
s = Square()
amount = 10000000
count = 0
for i in range(amount):
    if i % 1_000_000 == 0:
        print(i)
        print(c.comparer_runtime)
    if c.within_circle(*random_spawn()):
        count += 1
print(f'pi estimation: {(count / amount) * 4}')
print(math.pi)
