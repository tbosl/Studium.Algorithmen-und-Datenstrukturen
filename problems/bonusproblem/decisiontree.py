from random import random

from problems.bonusproblem.DataModel import Dataset
from problems.bonusproblem.Node import Node
from problems.bonusproblem.entropy import most_important_attribute, unique_values
from problems.bonusproblem.treeplot import TreePlot


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
        my_tree = Node(A, reason)
        values = []
        for e in examples:
            values.append(e.attributes[A])
        uv = unique_values(A, examples)
        for v in uv:
            exs = [e for e in examples if e.attributes[A] == v]
            subtree = dt_learning(exs, [a for a in attributes if a != A], examples)
            if subtree:
                subtree.reason = f"{A}: {v}"
            my_tree.insert(subtree)
    return my_tree


def plurality_val(examples):
    true_count = 0
    for e in examples:
        if e.decision is True or e.decision == 1:
            true_count += 1
    if true_count == len(examples) / 2:
        decision = random.Random().randint(0, 1)
    else:
        decision = 1 if true_count > len(examples / 2) else 0
    return Node(decision, "")


ds = Dataset(filepath="tables/attack.csv", decision="Attack")
tree = dt_learning(ds.items, ds.get_attributes(), ds.items, True)
tree.sort()
print(tree)
TreePlot().plot(tree, goal=ds.decision)
