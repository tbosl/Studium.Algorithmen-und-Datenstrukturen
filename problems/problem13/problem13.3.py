'''
Created on Apr 12, 2020

@author: pglauner
'''
import logging
import time

from map_table import MapBase, UnsortedTableMap
from random import randrange


class HashMapBase(MapBase):
    def __init__(self, cap=11, p=109345121):
        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) \
            % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v


class ChainHashMap(HashMapBase):
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error {0}'.format(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error {0}'.format(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                yield from bucket


def testMapString(myMap=ChainHashMap()):
    sTime = 0
    for i in range(1000):
        content = "abcdefghijklmnopqrstuvwxyz"
        key = ""
        for j in range(10):
            key += content[randrange(26)]
        value = ""
        for j in range(10):
            value += content[randrange(26)]
        storingStart = time.time_ns()
        myMap[key] = value
        sTime += time.time_ns() - storingStart
    printStart = time.time_ns()
    for key in myMap:
        logging.log(level=1, msg=f"{key}, {myMap[key]}")
    printTime = time.time_ns() - printStart
    print("Storing time: ", sTime / 1000)
    print("Printing time: ", printTime / 1000)


def testMapNumberSmall(myMap=ChainHashMap()):
    sTime = 0
    for i in range(1000):
        key = randrange(1000)
        value = randrange(1000)
        storingStart = time.time_ns()
        myMap[key] = value
        sTime += time.time_ns() - storingStart

    printStart = time.time_ns()
    for key in myMap:
        logging.log(level=1, msg=f"{key}, {myMap[key]}")

    printTime = time.time_ns() - printStart
    print("Storing time: ", sTime / 1000)
    print("Printing time: ", printTime / 1000)


def testMapNumberBig(myMap=ChainHashMap()):
    sTime = 0
    for i in range(1000):
        key = randrange(1000000)
        value = randrange(1000000)
        storingStart = time.time_ns()
        myMap[key] = value
        sTime += time.time_ns() - storingStart
    printStart = time.time_ns()
    for key in myMap:
        logging.log(level=1, msg=f"{key}, {myMap[key]}")
    printTime = time.time_ns() - printStart
    print("Storing time: ", sTime / 1000)
    print("Printing time: ", printTime / 1000)


testMapString()
testMapNumberSmall()
testMapNumberBig()

# Storing of strings take the longest time, followed by storing of big numbers and small numbers.
# Printing however is almost equivalent for all three cases.
# The reason is probably that the storing of a string takes longer than storing a number.
