from collections.abc import MutableMapping


class MapBase(MutableMapping):
    class _Item:
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)  # reuse implemented logic

        def __lt__(self, other):
            return self._key < other._key
