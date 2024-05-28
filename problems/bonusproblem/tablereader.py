import csv


def attributes_from_row(row, decision_attribute):
    attributes = {}
    for item in row:
        if item == decision_attribute:
            continue
        attributes[item] = row[item]
    return attributes


def read_csv_table(file_path, decision_attribute):
    items = []
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Create a Person object from the row
            decision = row[decision_attribute]
            attributes = attributes_from_row(row, decision_attribute)
            items.append((decision, attributes))
    return items

# read_table("temp.csv", "city")
# read_table("attack.csv", "Attack")
