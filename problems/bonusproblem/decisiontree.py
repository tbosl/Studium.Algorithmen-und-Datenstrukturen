from random import Random

from problems.bonusproblem.DataModel import Dataset
from problems.bonusproblem.Node import Node
from problems.bonusproblem.entropy import most_important_attribute, positive_results
from util import unique_values, check_if_all_examples_have_same_classification
from problems.bonusproblem.treeplot import TreePlot


def plurality_val(examples):
    true_count = 0
    for e in examples:
        if e.classification in positive_results:
            true_count += 1
    if true_count == len(examples) / 2:
        decision = Random().randint(0, 1)
    else:
        decision = 1 if true_count > len(examples / 2) else 0
    return Node(decision, "")


def dt_learning(examples: list, attributes, parent_examples, start=False):
    if not examples:
        return plurality_val(parent_examples)
    elif check_if_all_examples_have_same_classification(examples):
        return Node(examples[0].classification, "")
    elif not attributes:
        return plurality_val(examples)
    else:
        A = most_important_attribute(examples, attributes)[0]
        reason = A if not start else "root"
        my_tree = Node(A, reason)
        for v in unique_values(A, examples):
            exs = [e for e in examples if e.attributes[A] == v]
            subtree = dt_learning(exs, [a for a in attributes if a != A], examples)
            if subtree:
                subtree.reason = f"{A}: {v}"
            my_tree.insert(subtree)
    return my_tree


ds = Dataset(filepath="tables/attack.csv", decision="Attack")
tree = dt_learning(ds.items, ds.get_attributes(), ds.items, True)
tree.sort()
TreePlot().plot(tree, goal=ds.decision)
