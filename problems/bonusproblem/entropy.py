import math

from problems.bonusproblem.util import unique_values

positive_results = [True, 1, "T", "True", "t", "true", "TRUE", "yes", "Yes", "YES", "y", "Y", "1"]


def __p_goal_with_attribute(attribute, examples, value):
    matches = [e for e in examples if e.attributes[attribute] == value]
    positives = len([m for m in matches if m.classification in positive_results])
    return positives / len(matches)


def __entropy(attribute, examples, value):
    goal_ratio = __p_goal_with_attribute(attribute, examples, value)
    return __b(goal_ratio)


def __cardinality_ratio(A, a, examples):
    example_subset = [e for e in examples if e.attributes[A] == a]
    return len(set(example_subset)) / len(set(examples))


def __remainder(A, examples):
    return sum([__cardinality_ratio(A, a, examples) * __entropy(A, examples, a) for a in unique_values(A, examples)])


def __goal_possibilities(A, examples):
    sub_examples = [e for e in examples if A in e.attributes]
    count_pos = len([e for e in sub_examples if e.classification in positive_results])
    count = len(sub_examples)
    return count_pos / count


def __b(ratio):
    if ratio in [0, 1]:
        return 0
    return -(ratio * math.log2(ratio) + (1 - ratio) * math.log2(1 - ratio))


def __information_gain(A, examples):
    return __b(__goal_possibilities(A, examples)) - __remainder(A, examples)


def most_important_attribute(examples, attributes):
    max_gain = max((__information_gain(attribute, examples), attribute) for attribute in
                   attributes)  # max returns tuple where first element is max
    return [max_gain[1], max_gain[0]]
