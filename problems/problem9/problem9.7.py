class LinkedQueue:
    class MyNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self._head = None

    def enqueue(self, data):
        new_node = self.MyNode(data)
        if self._head is None:
            self._head = new_node
        else:
            new_node.next = self._head
            self._head = new_node

    def dequeue(self):
        if self._head is None:
            raise IndexError('List is empty')
        previous = None
        current_node = self._head
        while current_node.next is not None:
            previous = current_node
            current_node = current_node.next

        if previous is None:
            self._head = None
            return current_node.data

        previous.next = None
        return current_node.data


l = LinkedQueue()
l.enqueue(5)
l.enqueue(6)
l.enqueue(7)
l.enqueue(8)
print(l.dequeue())
print(l.dequeue())
print(l.dequeue())
l.enqueue(9)
print(l.dequeue())
print(l.dequeue())
