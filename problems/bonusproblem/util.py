def unique_values(A, examples):
    return set([e.attributes[A] for e in examples])


def check_if_all_examples_have_same_classification(examples):
    return len([e for e in examples if e.classification != examples[0].classification]) == 0
