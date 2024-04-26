class MyList:
    def __init__(self):
        self._data = []

    def append(self, e):
        self._data.append(e)

    def remove(self, e):
        self._data.remove(e)

    def remove_all(self, e):
        for i in range(len(self._data) - 1, -1, -1):
            if self._data[i] == e:
                del self._data[i]
                # for j in range(i, len(self._data) - 1):
                #     self._data[j] = self._data[j + 1]
                # self._data.pop()
                # self._data.


l = MyList()
l.append(5)
l.append(4)
l.append(3)
l.append(5)
l.append(1)
print(l._data)
l.remove_all(5)
print(l._data)
