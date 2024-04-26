class Converter:
    def __init__(self, expression):
        self._expression = expression
        self._operators = ['+', '-', '*', '/']

    def prepare_value_pairs(self):
        current_value = 0
        second_last = ""
        last = ""
        for i in range(len(self._expression)):
            item = self._expression[i]
            if item != " ":
                if item not in self._operators:
                    second_last = int(last) if last != '' else ''
                    last = int(item)
                else:
                    if i >= len(self._expression) - 1 or (
                            i < len(self._expression) - 1 and self._expression[i + 1] not in self._operators):
                        last = self.operation_on_numbers(second_last, last, item)
                        if i == 4:
                            current_value += last
                        # else:
                        #     self.operation_on_numbers(current_value, )

        return current_value

    def operation_on_numbers(self, second_last, last, operator):
        if operator == '+':
            return second_last + last
        elif operator == '-':
            return second_last - last
        elif operator == '*':
            return second_last * last
        else:
            return second_last / last


e = input("Your expression: ")
c = Converter(e)
print(c.prepare_value_pairs())
