import ctypes


class MyArray:
    def __init__(self):
        self._n = 0  # private vars indicated with _
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):  # overwrites
        return self._n

    def __getitem__(self, k):  # overwrites item[k]
        if not 0 <= k < self._n:  # not capacity because we don't want to check for placeholders
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]  # in C or C++ this would fill the RAM, so manually freeing necessary
        self._A = B  # Garbage collection takes care of old A
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()  # irrelevant how it works for us


data = MyArray()
len(data)
print(data._capacity)
data.append(200)
print(len(data))
data.append(300)
print(len(data))
print(data._capacity)
print(data[0])
data.append(400)
print(len(data))
print(data._capacity)