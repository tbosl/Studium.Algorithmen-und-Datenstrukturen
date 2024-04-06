# Give a big-Oh characterization, in terms of n, of the running time of the
# example5 function shown in Code Fragment 3.10
#  def example5(A, B): # assume that A and B have equal length
# 37 ”””Return the number of elements in B equal to the sum of prefix sums in A.”””
# 38 n = len(A)
# 39 count = 0
# 40 for i in range(n): # loop from 0 to n-1 (*n)
# 41 total = 0
# 42 for j in range(n): # loop from 0 to n-1 (*n*n)
# 43 for k in range(1+j): # loop from 0 to j (n * (1 + 2 + ... + n) --> n * (n+1)n /2 = n* (n²+n)/2 = (n³ + n²)/2
#                                                                                     --> ignore n² and 2 --> n³
# 44 total += A[k]
# 45 if B[i] == total:
# 46 count += 1
# 47 return count
# O(n³)
