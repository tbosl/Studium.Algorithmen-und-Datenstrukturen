import ctypes


class MyArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1

        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def __setitem__(self, k, v):
        if k < 0:
            raise IndexError('invalid index')
        while self._capacity <= k:
            self._resize(2 * self._capacity)
        if self._n < k + 1:
            self._n = k + 1
        self._A[k] = v

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, v):
        if k < 0:
            raise IndexError('invalid index')
        if self._capacity <= k:
            self._resize(2 * self._capacity)
        for i in range(self._n - 1, k + 1, -1):
            print(i)
            self._A[i] = self._A[i - 1]
        if self._n < k + 1:
            self._n = k + 1
        self._A[k] = v

    def remove(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        for i in range(k + 1, self._n - 1):
            self._A[i] = self._A[i + 1]
        self._A[self._n] = None
        threshold_percentage = 10
        all_empty = True
        for i in range(self._n // threshold_percentage, self._n - 1):
            if not self._A[i]:
                all_empty = False
            self._n = i + 1
        if all_empty:
            self._resize(0.5 * self._capacity)

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
print(a[0])
a[10] = 10
print_array(a)
a.insert(5, 5)
print_array(a)
