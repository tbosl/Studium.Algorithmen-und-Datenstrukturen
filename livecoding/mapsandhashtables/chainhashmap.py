from livecoding.mapsandhashtables.hashmapbase import HashMapBase
from livecoding.mapsandhashtables.unsortedtablemap import UnsortedTableMap


class ChainHashMap(HashMapBase):
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error {0}'.format(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])  # len of the unsorted table map (the bucket)
        self._table[j][k] = v  # uses setitem of unsorted table map
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error {0}'.format(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:  # empty means there is no unsorted table map
                yield from bucket  # uses generator delegation to use the _iter__ method from the unsorted table map


ht1 = ChainHashMap()
print(len(ht1))
ht1[1] = 'One'
ht1[2] = 'Two'
print(len(ht1))
ht1[2] = 'Two!'
print(ht1[2])
del ht1[2]
print(len(ht1))
