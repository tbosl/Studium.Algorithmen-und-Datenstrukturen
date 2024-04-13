import ctypes


class MyArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1

        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if abs(k) >= self._n:
            raise IndexError('invalid index')
        if k < 0:
            k = self._n + k
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)

        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()


def print_array(a):
    output = '[ '
    for i in range(len(a)):
        try:
            output += str(a[i]) + ', '
        except ValueError:
            output += 'Null, '
    output += ']'
    print(output)


a = MyArray()
print(len(a))
a.append(5)
a.append(6)
a.append(7)
a.append(8)
print(a[-1])