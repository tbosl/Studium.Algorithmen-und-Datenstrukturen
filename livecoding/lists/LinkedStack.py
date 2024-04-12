class Empty(Exception):
    pass


class LinkedStack:
    class _Node:
        def __init__(self, element, next_element):
            self._element = element
            self._next_element = next_element

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        res = self._head._element
        self._head = self._head._next_element
        self._size -= 1
        return res


l = LinkedStack()
l.push(1)
l.push(2)
l.pop()
