# Show that sum from i=1 to n of i = n(n+1)/2
# and n(n+1)/2 is O(n²)

# P(n) === sum from i=1 to n of i = n(n+1)/2
# IB: P(1): 1 = 1 | yes
# IA: There exists an n in N for which P(n) holds
# IS: P(n) => P(n+1)
# sum of i from 1 to n + 1 = (n+1)(n+2)/2
# sum of i from 1 to n + (n+1) = (n+1)(n+2)/2
# <=> IA
# n(n+1)/2 + (n+1) = (n+1)(n+2)/2
# [n(n+1) + 2(n+1)]/2 = (n+1)(n+2)/2
# (n+1)(n+2)/2 = (n+1)(n+2)/2 | yes

# => Induction is true
# (n+1)(n+2)/2 = (n²+3n+2)/2
# => fastest growing is n² --> (n+1)(n+2)/2 is O(n²)
# with c = 2 and n0 = 2
