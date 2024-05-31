from problems.bonusproblem.tablereader import read_csv_table

# The possible result values of a positive classification.
positive_results = [True, 1, "T", "True", "t", "true", "TRUE", "yes", "Yes", "YES", "y", "Y", "1"]


class DataItem:
    """A class representing a data item."""

    def __init__(self, classification, attributes):
        """Initializes the data item with the given classification and attributes.
         Attributes is a dictionary of attribute names to the value in the item"""
        self.classification = classification
        self.attributes = attributes


class Dataset:
    """A class representing a dataset."""

    def __init__(self, filepath, decision):
        """Initializes the dataset with the by reading the table at filepath.
           The decision is the name of the classification attribute."""
        self.items = [DataItem(classification=item[0], attributes=item[1]) for item in
                      read_csv_table(filepath, decision)]
        self.decision = decision
        self.positive = None
        self.negative = None

    def get_attributes(self):
        """Returns the attributes of the dataset."""
        return [key for key in self.items[0].attributes]

    def positive_classification(self):
        """Returns the presentation of a positive classification in the dataset."""
        if self.positive:
            return self.positive
        for i in self.items:
            if i.classification in positive_results:
                self.positive = i.classification
                return self.positive

    def negative_classification(self):
        """Returns the presentation of a negative classification in the dataset."""
        if self.negative:
            return self.negative

        for i in self.items:
            if i.classification not in positive_results:
                self.negative = i.classification
                return self.negative
