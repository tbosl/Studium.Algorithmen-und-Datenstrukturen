from random import Random
import time


def quick_sort_class(S):
    if len(S) <= 1:
        return S
    left = []
    right = []
    pivot = S[0]  # left-most or right-most -> does not matter
    for element in S:
        if element >= pivot:
            right.append(element)
        else:
            left.append(element)
    left = quick_sort_class(left)
    right = quick_sort_class(right[1:])  # all elements but skipping index 0 (pivot - don't want to process further)
    return left + [pivot] + right


def quick_sort_random(S):
    if len(S) <= 1:
        return S
    left = []
    right = []
    pivot = S[Random().randint(0, len(S) - 1)]  # left-most or right-most -> does not matter
    for element in S:
        if element >= pivot:
            right.append(element)
        else:
            left.append(element)
    left = quick_sort_class(left)
    right = quick_sort_class(right[1:])  # all elements but skipping index 0 (pivot - don't want to process further)
    return left + [pivot] + right


def run_class(data):
    start_time = time.time()
    data_sorted = quick_sort_class(data)
    run_time = time.time() - start_time
    # print("Class: " + str(run_time))
    # print(data_sorted)
    return run_time * 1000


def run_random(data):
    start_time = time.time()
    data_sorted = quick_sort_random(data)
    run_time = time.time() - start_time
    # print("Random: " + str(run_time))
    # print(data_sorted)
    return run_time * 1000


def run_comparison(data):
    global r
    global c
    class_time = run_class(data)
    random_time = run_random(data)
    if class_time < random_time:
        print("Class: \n" + str(class_time) + " vs. \n" + str(random_time))
        c += 1
    else:
        print("Random: \n" + str(random_time) + " vs. \n" + str(class_time))
        r += 1


r = 0
c = 0

for i in range(10):
    # data = [85, 24, 63, 45, 17, 31, 96, 50]
    d = [Random().randint(0, 10000) for _ in range(10000)]
    run_comparison(d)

print(str(r) + " vs. " + str(c))

r = 0
c = 0

print("________________SORTED________________")
for j in range(10000):
    d = [i for i in range(800)]
    run_comparison(d)

# unsorted: runtime difference maximum 1ms most of the time
# sometimes random faster, sometimes class (almost 50:50 on 10.000 runs)

# sorted: random almost always faster sometimes more than twice as fast
# 9546 : 464 on 10.000 runs
