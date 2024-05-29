import csv


def __attributes_from_row(row, classification_attribute):
    return {attribute: value for (attribute, value) in row.items() if attribute != classification_attribute}


def read_csv_table(file_path, decision_attribute):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        return [(row[decision_attribute], __attributes_from_row(row, decision_attribute)) for row in csv_reader]
