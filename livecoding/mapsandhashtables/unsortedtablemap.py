from livecoding.mapsandhashtables.map import MapBase


class UnsortedTableMap(MapBase):
    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __setitem__(self, k, v):  # unsorted so no ordering necessary
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k, v))

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error {0}'.format(k))

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)  # pop good? On ArrayLists pop works best for right most element.
                # In the middle we have to shift all remaining elements to the left.
                return
        raise KeyError('Key Error {0}'.format(k))


map1 = UnsortedTableMap()
map1[1] = 'One'
map1[2] = 'Two'
print(map1[1])
print(map1[2])
# print(map1[3])  # KeyError
print(len(map1))
del map1[1]
print(len(map1))  # KeyError
map1[1] = 'One!'
print(map1[1])
