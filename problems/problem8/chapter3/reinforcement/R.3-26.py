# 6 Give a big-Oh characterization, in terms of n, of the running time of the
# example4 function shown in Code Fragment 3.10.
# def example4(S):
# 27 ”””Return the sum of the prefix sums of sequence S.”””
# 28 n = len(S)
# 29 prefix = 0
# 30 total = 0
# 31 for j in range(n):
# 32 prefix += S[j]
# 33 total += prefix
# 34 return total
# O(n)
def example4(S):
    n = len(S)
    prefix = ''
    total = ''
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total


print(example4('Hello'))
