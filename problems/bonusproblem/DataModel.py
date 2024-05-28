from problems.bonusproblem.tablereader import read_csv_table


class DataItem:
    def __init__(self, decision, attributes):
        self.decision = decision
        self.attributes = attributes

    def __repr__(self):
        return f"{self.decision} | {self.attributes}"


class Dataset:
    def __init__(self, filepath, decision):
        self.items = []
        self.decision = decision
        for item in read_csv_table(filepath, decision):
            self.items.append(DataItem(item[0], item[1]))
        # self.items = [
        #     DataItem(True, {"v": 0, "d": "< 10", "a": 0}),
        #     DataItem(False, {"v": 0, "d": "< 10", "a": 1}),
        #     DataItem(False, {"v": 0, "d": "10 - 20", "a": 0}),
        #     DataItem(False, {"v": 0, "d": "10 - 20", "a": 1}),
        #     DataItem(False, {"v": 0, "d": "> 20", "a": 0}),
        #     DataItem(False, {"v": 0, "d": "> 20", "a": 1}),
        #     DataItem(True, {"v": 1, "d": "< 10", "a": 0}),
        #     DataItem(True, {"v": 1, "d": "< 10", "a": 1}),
        #     DataItem(True, {"v": 1, "d": "10 - 20", "a": 0}),
        #     DataItem(True, {"v": 1, "d": "10 - 20", "a": 1}),
        #     DataItem(False, {"v": 1, "d": "> 20", "a": 0}),
        #     DataItem(False, {"v": 1, "d": "> 20", "a": 1})
        # ]

    def get_attributes(self):
        return [key for key in self.items[0].attributes]
