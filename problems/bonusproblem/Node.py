class Node:
    def __init__(self, data, reason):
        self.children = []
        self.data = data
        self.reason = reason

    def insert(self, subtree):
        self.children.append(subtree)

    @staticmethod
    def __sort_by_keys(atc):
        return {k: atc[k] for k in sorted((atc.keys()))}

    def __value_from_reason(self):
        return self.reason[self.reason.index(":") + 1:].strip()

    def sort(self):
        values_to_children = {c.__value_from_reason(): c for c in self.children}
        ordered_values = self.__sort_by_keys(values_to_children)
        self.children = list(ordered_values.values())
        for child in self.children:
            child.sort()

    def __repr__(self):
        return f"{self.reason} -> {self.data}"
