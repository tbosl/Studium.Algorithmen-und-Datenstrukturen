import math


def entropy(attribute, examples, value):
    goal_ratio = p_goal_with_attribute(attribute, examples, value)
    return B(goal_ratio)


def p_goal_with_attribute(attribute, examples, value):
    matches = [e for e in examples if e.attributes[attribute] == value]
    positives = 0
    for m in matches:
        if m.decision is True or m.decision == 1 or m.decision == "T":
            positives += 1
    return positives / len(matches)


def unique_values(A, examples):
    values = []
    for e in examples:
        values.append(e.attributes[A])
    return set(values)


def remainder(A, examples):
    r = 0
    uv = unique_values(A, examples)
    for a in uv:
        ek = [e for e in examples if e.attributes[A] == a]
        cardinality_ratio = (len(set(ek)) / len(set(examples)))
        current_entropy = entropy(A, examples, a)
        r += cardinality_ratio * current_entropy
    return r


def goal_possibilities(A, examples):
    count_pos = 0
    count = 0
    for e in examples:
        if A in e.attributes:
            count += 1
            if e.decision is True or e.decision == 1 or e.decision == "T":
                count_pos += 1
    return count_pos / count


def B(ratio):
    if ratio == 1 or ratio == 0:
        return 0
    return -(ratio * math.log2(ratio) + (1 - ratio) * math.log2(1 - ratio))


# goal probably decision
def information_gain(A, examples):
    b_goal = B(goal_possibilities(A, examples))
    return b_goal - remainder(A, examples)


def most_important_attribute(examples, attributes):
    max_gain = ["", -1]
    for attribute in attributes:
        gain = information_gain(attribute, examples)
        if gain > max_gain[1]:
            max_gain = [attribute, gain]
    return max_gain
