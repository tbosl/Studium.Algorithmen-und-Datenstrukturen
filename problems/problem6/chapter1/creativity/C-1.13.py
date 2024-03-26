import time


def reverse(data):
    for i in range(len(data) // 2):
        data[i], data[len(data) - 1 - i] = data[len(data) - 1 - i], data[i]


d = [1, 2, 3, 4, 5, 6, 7]
d = [i for i in range(1000)]
print(d)
start = time.perf_counter_ns()
reverse(d)
end = time.perf_counter_ns()
print(d)
print("Time " + str(end - start))

start = time.perf_counter_ns()
d = list(reversed(d))
end = time.perf_counter_ns()
print(d)
print("Time " + str(end - start))
