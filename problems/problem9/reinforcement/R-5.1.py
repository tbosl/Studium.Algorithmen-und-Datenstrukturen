import sys # provides getsizeof function
data = [ ]
n = 27
for k in range(n): # NOTE: must fix choice of n
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.append(None) # increase length by one

# Comparison: My arrays are smaller and the increments are also smaller from 17 bytes on
# However, the intervals in both cases have the same length

### My results:
# Length:   0; Size in bytes:   56
# Length:   1; Size in bytes:   88
# Length:   2; Size in bytes:   88
# Length:   3; Size in bytes:   88
# Length:   4; Size in bytes:   88
# Length:   5; Size in bytes:  120
# Length:   6; Size in bytes:  120
# Length:   7; Size in bytes:  120
# Length:   8; Size in bytes:  120
# Length:   9; Size in bytes:  184
# Length:  10; Size in bytes:  184
# Length:  11; Size in bytes:  184
# Length:  12; Size in bytes:  184
# Length:  13; Size in bytes:  184
# Length:  14; Size in bytes:  184
# Length:  15; Size in bytes:  184
# Length:  16; Size in bytes:  184
# Length:  17; Size in bytes:  248
# Length:  18; Size in bytes:  248
# Length:  19; Size in bytes:  248
# Length:  20; Size in bytes:  248
# Length:  21; Size in bytes:  248
# Length:  22; Size in bytes:  248
# Length:  23; Size in bytes:  248
# Length:  24; Size in bytes:  248
# Length:  25; Size in bytes:  312
# Length:  26; Size in bytes:  312


### Book result:
# Length: 0; Size in bytes: 72
# Length: 1; Size in bytes: 104
# Length: 2; Size in bytes: 104
# Length: 3; Size in bytes: 104
# Length: 4; Size in bytes: 104
# Length: 5; Size in bytes: 136
# Length: 6; Size in bytes: 136
# Length: 7; Size in bytes: 136
# Length: 8; Size in bytes: 136
# Length: 9; Size in bytes: 200
# Length: 10; Size in bytes: 200
# Length: 11; Size in bytes: 200
# Length: 12; Size in bytes: 200
# Length: 13; Size in bytes: 200
# Length: 14; Size in bytes: 200
# Length: 15; Size in bytes: 200
# Length: 16; Size in bytes: 200
# Length: 17; Size in bytes: 272
# Length: 18; Size in bytes: 272
# Length: 19; Size in bytes: 272
# Length: 20; Size in bytes: 272
# Length: 21; Size in bytes: 272
# Length: 22; Size in bytes: 272
# Length: 23; Size in bytes: 272
# Length: 24; Size in bytes: 272
# Length: 25; Size in bytes: 272
# Length: 26; Size in bytes: 352
