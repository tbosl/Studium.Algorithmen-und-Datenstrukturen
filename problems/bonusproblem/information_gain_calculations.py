import math

from problems.bonusproblem.util import unique_values
from DataModel import positive_results


def ratio_of_positive_classification_for_attribute_value(attribute, examples, value):
    """Returns the ratio of positive classifications for the given attribute value."""
    matches = [e for e in examples if e.attributes[attribute] == value]
    positives = len([m for m in matches if m.classification in positive_results])
    return positives / len(matches)


def entropy(attribute, examples, value):
    """Returns the entropy of the given attribute value."""
    goal_ratio = ratio_of_positive_classification_for_attribute_value(attribute, examples, value)
    return b(goal_ratio)


def cardinality_ratio(A, a, examples):
    """Returns the ratio of the cardinality of the subset of examples where the attribute A
    has the value a compared to the cardinality of the set of examples."""
    example_subset = [e for e in examples if e.attributes[A] == a]
    return len(set(example_subset)) / len(set(examples))


def remainder(A, examples):
    """Returns the expected remaining entropy after testing the attribute A."""
    return sum([cardinality_ratio(A, a, examples) * entropy(A, examples, a) for a in unique_values(A, examples)])


def positive_goal_possibility(examples):
    """Returns the ratio of positive classifications in the examples."""
    count_pos = len([e for e in examples if e.classification in positive_results])
    return count_pos / len(examples)


def b(positive_goal_ratio):
    """Returns the entropy of the given ratio of positive classifications."""
    if positive_goal_ratio in [0, 1]:
        return 0
    return -(positive_goal_ratio * math.log2(positive_goal_ratio) + (1 - positive_goal_ratio) * math.log2(
        1 - positive_goal_ratio))


def information_gain(A, examples):
    """Returns the information gain of the attribute A."""
    return b(positive_goal_possibility(examples)) - remainder(A, examples)


def most_important_attribute(examples, attributes):
    """Returns the attribute with the highest information gain and its information gain."""
    max_gain = max((information_gain(attribute, examples), attribute) for attribute in
                   attributes)  # max returns tuple where first element is max
    return [max_gain[1], max_gain[0]]
