import csv


def attributes_from_row(items, classification_attribute):
    """Returns a dictionary of attributes from a row, excluding the classification attribute."""
    return {attribute: value for (attribute, value) in items if attribute != classification_attribute}


def read_csv_table(file_path, decision_attribute):
    """Returns a list of tuples with the classification attribute
     and a dictionary of attributes from the rows in the file."""
    with open(file_path, mode='r', newline='') as file:
        return [(row[decision_attribute], attributes_from_row(row.items(), decision_attribute)) for row in
                csv.DictReader(file) if isinstance(row, dict)]
