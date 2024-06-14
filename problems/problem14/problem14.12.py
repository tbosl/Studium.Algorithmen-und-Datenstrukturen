import struct


def inverse_sqrt(x):
    threehalfs = 1.5
    x2 = x * 0.5
    y = x

    # Pack the float into bytes, then unpack as int to get the binary representation
    i = struct.unpack('i', struct.pack('f', y))[0]

    # Apply the magic number and bitwise operations
    i = 0x5f3759df - (i >> 1)

    # Pack the int back into bytes, then unpack as float to get the modified float value
    y = struct.unpack('f', struct.pack('i', i))[0]
    y = y * (threehalfs - (x2 * y * y))  # newton method one iteration
    return y


print(inverse_sqrt(25))
print(inverse_sqrt(712311))
