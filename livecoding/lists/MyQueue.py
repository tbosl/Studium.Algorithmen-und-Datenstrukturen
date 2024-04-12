class Empty(Exception):
    pass


class MyQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        # self._data = []
        self._data = [None] * MyQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._size -= 1
        self._data[self._front] = None
        # self._size = self._size + 1 if self._size + 1 < len(self) else 0
        self._size = (self._size + 1) % len(self._data)
        self._front += 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0


# def enqueue(self, e):
#     self._data.append(e)
#     self._size += 1
#
# def dequeue(self):
#     if self.is_empty():
#         raise Empty('Queue is empty')
#     self._data.pop(0)  # not good: Theta(n)


q = MyQueue()
print(len(q))
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(len(q))
print(q._data)
print(q.dequeue())
print(q._data)
print(q.dequeue())
print(q._data)
print(q.dequeue())
print(q._data)
print(q.dequeue())
