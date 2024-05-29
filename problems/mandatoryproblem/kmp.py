import time


def findkmp(T, P):
    """Return the lowest
    index of T at which substring P begins(or else - 1)."""

    n, m = len(T), len(P)  # introduce convenient notations
    if m == 0:
        return 0  # trivial search for empty string

    fail = compute_kmp_fail(P)  # rely on utility to precompute

    j = 0  # index into text
    k = 0  # index into pattern

    while j < n:
        if T[j] == P[k]:  # P[0:1+k] matched thus far
            if k == m - 1:  # match is complete
                return j - m + 1
            j += 1  # try to extend match
            k += 1

        elif k > 0:
            k = fail[k - 1]  # reuse suffix of P[0:k]
        else:
            j += 1

    return -1  # reached end without match


def compute_kmp_fail(P):
    """Utility that computes and returns KMP fail list."""
    m = len(P)
    fail = [0] * m  # by default,presume overlap of 0 everywhere
    j = 1
    k = 0
    while j < m:  # compute f(j) during this pass, if nonzero
        if P[j] == P[k]:  # k+1 characters match thus far
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:  # k follows a matching prefix
            k = fail[k - 1]
        else:  # no match found starting at j
            j += 1
    return fail


words_a = ["Everspring",
           "Alaric",
           "Liora",
           "Great Oak",
           "innovation",
           "harmony",
           "progress",
           "tradition",
           "villagers",
           "Elara"]

words_b = [" Let G be",
           "An execution of Dijkstra’s",
           "Recalling the definition"
           ]

words_c = [" by the stinging commentary",
           "because he really had something new to say",
           "labored",
           "interpreted for them by the stinging commentary of some infringement",
           "The correspondence of Pope is, on the whole, less interesting than that of any other eminent English poet, except that of Southey, and their letters have the same fault of being labored compositions. Southey’s are, on the whole, the more agreeable of the two, for they inspire one",
           "correspondence of Pope is, on the whole, less interesting than that of any other eminent English poet, except that of Southey, and their letters have the same fault of being labored compositions. Southey’s are, on the whole, the more agreeable of the two, for they inspire one"]

enc = "utf-8"
text = open("example2.txt", "r", encoding=enc).read()
durations = []
iterations = 100  # Anzahl der Wiederholungen pro Wort
durations = []

for word in words_c:
    total_duration = 0
    for _ in range(iterations):
        start = time.time_ns()
        index = findkmp(text, word)
        end = time.time_ns()
        total_duration += (end - start)
    avg_duration = total_duration / iterations
    print(f"{index}: {text[index:index + len(word)]}")
    print(avg_duration)
    durations.append(avg_duration)

print(f"avg: {sum(durations) / len(durations)}")

# print(findkmp("Hello I am Tobi", "I"))
