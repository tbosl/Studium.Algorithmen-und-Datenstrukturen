# Give a big-Oh characterization, in terms of n, of the running time of the
# example2 function shown in Code Fragment 3.10
#  def example2(S):
# 10 ”””Return the sum of the elements with even index in sequence S.”””
# 11 n = len(S)
# 12 total = 0
# 13 for j in range(0, n, 2): # note the increment of 2
# 14 total += S[j]
# 15 return total
# O(n/2) --> O(n)
