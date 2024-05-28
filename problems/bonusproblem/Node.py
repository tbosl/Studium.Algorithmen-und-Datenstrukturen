class Node:
    def __init__(self, data, reason):
        self.children = []
        self.data = data
        self.reason = reason  # will be key + value of the attribute (e. g. v : 0) -> text in tree

    def insert(self, subtree):
        self.children.append(subtree)

    @staticmethod
    def sort_attributes(atc):
        ordered = {}
        for k in sorted(atc.keys()):
            ordered[k] = atc[k]
        return ordered

    def sort(self):
        attributes_to_children = {}
        for c in self.children:
            attributes_to_children[c.reason[c.reason.index(":") + 1:].strip()] = c
        ordered_attributes = self.sort_attributes(attributes_to_children)
        ordered_children = [ordered_attributes[x] for x in ordered_attributes]
        self.children = ordered_children
        for child in self.children:
            child.sort()

    def __repr__(self):
        return f"{self.reason} -> {self.data}"
