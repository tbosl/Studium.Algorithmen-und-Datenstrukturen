class Node:
    """A node in a decision tree."""

    def __init__(self, data, reason):
        """Initializes a node with the given data and reason."""
        self.children = []
        self.data = data
        self.reason = reason

    def insert(self, subtree):
        """Adds the provided subtree to the children list of the node."""
        self.children.append(subtree)

    @staticmethod
    def __sort_by_keys(atc):
        """Returns a sorted dictionary based on the keys of the given dictionary."""
        return {k: atc[k] for k in sorted((atc.keys()))}

    def __value_from_reason(self):
        """The value of the most important attribute of
           the parent used by the root of this subtree."""
        return self.reason[self.reason.index(":") + 1:].strip()

    def sort(self):
        """Sorts the children of this node."""
        values_to_children = {c.__value_from_reason(): c for c in self.children}
        ordered_values = self.__sort_by_keys(values_to_children)
        self.children = list(ordered_values.values())
        for child in self.children:
            child.sort()

    def __repr__(self):
        return f"{self.reason} -> {self.data}"
