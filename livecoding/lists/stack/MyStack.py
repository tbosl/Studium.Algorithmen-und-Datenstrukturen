class Empty(Exception):
    pass


class MyStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


s = MyStack()
print(len(s))
s.push(4)
s.push(3)
s.push(2)
print(len(s))
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
