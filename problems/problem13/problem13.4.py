from random import randrange

from map_table import MapBase


class HashMapBase(MapBase):
    def __init__(self, cap=11, p=109345121):
        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)

    def hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self.table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self.hash_function(k)
        return self.bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self.hash_function(k)
        self.bucket_setitem(j, k, v)
        if self.n > len(self.table) // 2:
            self.resize(2 * len(self.table) - 1)

    def __delitem__(self, k):
        j = self.hash_function(k)
        self.bucket_delitem(j, k)
        self.n -= 1

    def resize(self, c):
        old = list(self.items())

        self._table = c * [None]
        self.n = 0
        for (k, v) in old:
            self[k] = v

# Review the generic hash table implementation in Algorithm 5. Explain why attribute n is updated in
# delitem (self, k) but not updated in setitem (self, k, v)
# It has to be updated in delitem because we are removing an item from the hash table.
# Since we make use of bucket_setitem we dont have to update n because this is done in the bucket_setitem method.
# The bucket_delitem does not update n
# Hence we have to update n in delitem but not in setitem
