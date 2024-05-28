from problems.bonusproblem.entropy import plurality_val, most_important_attribute, unique_values


class DataItem:
    def __init__(self, decision, attributes):
        self.decision = decision
        self.attributes = attributes

    def __repr__(self):
        return f"{self.decision} | {self.attributes}"


class Dataset:
    def __init__(self):
        self.items = [
            DataItem(True, {"v": 0, "d": "< 10", "a": 0}),
            DataItem(False, {"v": 0, "d": "< 10", "a": 1}),
            DataItem(False, {"v": 0, "d": "10 - 20", "a": 0}),
            DataItem(False, {"v": 0, "d": "10 - 20", "a": 1}),
            DataItem(False, {"v": 0, "d": "> 20", "a": 0}),
            DataItem(False, {"v": 0, "d": "> 20", "a": 1}),
            DataItem(True, {"v": 1, "d": "< 10", "a": 0}),
            DataItem(True, {"v": 1, "d": "< 10", "a": 1}),
            DataItem(True, {"v": 1, "d": "10 - 20", "a": 0}),
            DataItem(True, {"v": 1, "d": "10 - 20", "a": 1}),
            DataItem(False, {"v": 1, "d": "> 20", "a": 0}),
            DataItem(False, {"v": 1, "d": "> 20", "a": 1})
        ]

    def get_attributes(self):
        return [key for key in self.items[0].attributes]


class Node:
    def __init__(self, data, reason):
        self.children = []
        self.data = data
        self.reason = reason  # will be key + value of the attribute (e. g. v : 0) -> text in tree

    def insert(self, subtree):
        self.children.append(subtree)


def dt_learning(examples: list, attributes, parent_examples, start=False):
    examples_with_other_classification = [e for e in examples if e.decision != examples[0].decision]
    if not examples:
        return plurality_val(parent_examples)
    elif len(examples_with_other_classification) == 0:
        return Node(examples[0].decision, "")
    elif not attributes:
        return plurality_val(examples)
    else:
        A = most_important_attribute(examples, attributes)[0]
        reason = A if not start else "root"
        tree = Node(A, reason)
        values = []
        for e in examples:
            values.append(e.attributes[A])
        uv = unique_values(A, examples)
        for v in uv:
            exs = [e for e in examples if e.attributes[A] == v]
            subtree = dt_learning(exs, [a for a in attributes if a != A], examples)
            if subtree:
                subtree.reason = f"{A}: {v}"
            tree.insert(subtree)
    return tree


ds = Dataset()
tree = dt_learning(ds.items, ds.get_attributes(), ds.items, True)
print(tree)
