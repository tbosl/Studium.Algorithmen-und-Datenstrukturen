import sys # provides getsizeof function
data = [ ]
n = 1000

# The intervals are getting ever-larger
last_known_size = sys.getsizeof(data)
for k in range(n): # NOTE: must fix choice of n
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes
    if b != last_known_size:
        last_known_size = b
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.append(None) # increase length by one