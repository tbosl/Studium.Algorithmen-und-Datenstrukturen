# MutableMapping provides getitem , setitem , delitem , len , and iter .
# Use these to provide a pop implementation.
from collections.abc import MutableMapping


class MutableMappingWithPop(MutableMapping):
    def pop(self, k, default=None):
       try:
           value = self[k]
           del self[k]
           return value
       except KeyError:
           raise(KeyError(f'KeyError: {k}'))