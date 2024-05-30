from problems.bonusproblem.entropy import positive_results
from problems.bonusproblem.tablereader import read_csv_table


class DataItem:
    def __init__(self, classification, attributes):
        self.classification = classification
        self.attributes = attributes


class Dataset:
    def __init__(self, filepath, decision):
        self.items = [DataItem(classification=item[0], attributes=item[1]) for item in
                      read_csv_table(filepath, decision)]
        self.decision = decision
        self.positive = None
        self.negative = None

    def get_attributes(self):
        return [key for key in self.items[0].attributes]

    def positive_classification(self):
        if self.positive:
            return self.positive
        for i in self.items:
            if i.classification in positive_results:
                self.positive = i.classification
                return self.positive

    def negative_classification(self):
        if self.negative:
            return self.negative

        for i in self.items:
            if i.classification not in positive_results:
                self.negative = i.classification
                return self.negative
