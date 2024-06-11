from random import Random

from problems.bonusproblem.DataModel import Dataset
from problems.bonusproblem.Node import Node
from problems.bonusproblem.information_gain_calculations import most_important_attribute, positive_results
from util import unique_values, check_if_all_examples_have_same_classification
from problems.bonusproblem.treeplot import TreePlot


def plurality_val(examples):
    """Returns the most common classification in the examples. If there is a tie, a random decision is made."""
    true_count = len([e for e in examples if e.classification in positive_results])
    if true_count == len(examples) / 2:
        decision = Random().randint(0, 1)
    else:
        decision = ds.positive_classification() if true_count > len(examples) / 2 else ds.negative_classification()
    return Node(decision, "")


def dt_learning(examples: list, attributes, parent_examples, start=False):
    """Returns a decision tree based on the examples and attributes."""
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
