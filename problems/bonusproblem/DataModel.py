from problems.bonusproblem.tablereader import read_csv_table


def check_if_all_examples_have_same_classification(examples):
    return len([e for e in examples if e.classification != examples[0].classification]) == 0


class DataItem:
    def __init__(self, classification, attributes):
        self.classification = classification
        self.attributes = attributes

    def __repr__(self):
        return f"{self.classification} | {self.attributes}"


class Dataset:
    def __init__(self, filepath, decision):
        self.items = [DataItem(classification=item[0], attributes=item[1]) for item in read_csv_table(filepath, decision)]
        self.decision = decision

    def get_attributes(self):
        return [key for key in self.items[0].attributes]