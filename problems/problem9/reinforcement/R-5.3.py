import sys # provides getsizeof function
n = 1000
data = [None] * n

# The intervals are getting ever-smaller but at the same points whilst growing
last_known_size = sys.getsizeof(data)
for k in range(n): # NOTE: must fix choice of n
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes
    if b != last_known_size:
        last_known_size = b
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.pop() # increase length by one