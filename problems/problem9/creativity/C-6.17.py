class Empty(Exception):
    pass


class Full(Exception):
    pass


class ArrayStack:
    def __init__(self, maxlen=None):
        self._data = [None] * maxlen
        self._maxlen = maxlen

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        pushed = False
        for i in range(len(self._data)):
            if self._data[i] is None:
                self._data[i] = e
                pushed = True
                break
        if not pushed:
            raise Full('Stack is full')

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


a = ArrayStack(2)
a.push(2)
a.push(2)
print(a._data)
a.push(2)
