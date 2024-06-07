from collections.abc import MutableMapping


class MutableMappingWithItems(MutableMapping):
    def items(self):
        items = set()
        for key in self._table:
            items.add((key, self._table[key]))
        return items
