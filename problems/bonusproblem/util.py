def unique_values(A, examples):
    """Returns the unique values of the attribute A in the examples."""
    return set([e.attributes[A] for e in examples])


def check_if_all_examples_have_same_classification(examples):
    """Returns True if all examples have the same classification, False otherwise."""
    if not examples:
        return True
    return len([e for e in examples if e.classification != examples[0].classification]) == 0
