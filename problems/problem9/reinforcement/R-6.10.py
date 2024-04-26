# 48 def resize(self, cap): # we assume cap >= len(self)
# 49 ”””Resize to a new list of capacity >= len(self).”””
# 50 old = self. data # keep track of existing list
# 51 self. data = [None] cap # allocate list with new capacity
# 52 walk = self. front
# 53 for k in range(self. size): # only consider existing elements
# 54    self. data[k] = old[walk] # intentionally shift indices
# 55    walk = (1 + walk) % len(old) # use old size as modulus
# 56 self. front = 0 # front has been realigned

# Consider what happens if the loop in the ArrayQueue. resize method at
# lines 53–55 of Code Fragment 6.7 had been implemented as:
#   for k in range(self. size):
#       self. data[k] = old[k] # rather than old[walk]
# Give a clear explanation of what could go wrong.

# The new array will not be starting with front at index 0
# Therefore since we reset the front variable after the loop,
# the new array will remain in the same order as the original but the
# reference to the front element will no longer be the same.
# So, if element 10 was the front in the former implementation, it will become the first element of the
# new array and the front will be set to index 0.
# In the second implementation, the former front element will still be at index 10 but the index defined as front
# will be index 0. So the start point of the queue will change.
