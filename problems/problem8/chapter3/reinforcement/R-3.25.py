# Give a big-Oh characterization, in terms of n, of the running time of the
# example3 function shown in Code Fragment 3.10
# def example3(S):
# 18 ”””Return the sum of the prefix sums of sequence S.”””
# 19 n = len(S)
# 20 total = 0
# 21 for j in range(n): # loop from 0 to n-1
# 22 for k in range(1+j): # loop from 0 to j ((sum of 1 + 2 + ... + n)
#                   --> (n + 1)n / 2 --> (n² + n)/2 --> ignore n and 2 --> n²
# 23 total += S[k]
# 24 return total
# O(n²)
