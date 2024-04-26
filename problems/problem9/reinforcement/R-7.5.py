class MyCircularLinkedList:
    class MyNode:
        def __init__(self, data):
            self.next = None
            self.data = data

    def __init__(self):
        self._head = None
        self._tail = None

    def append(self, data):
        new_node = self.MyNode(data)
        if self._head is not None:
            self._head.next = new_node
        self._head = new_node
        if self._tail is None:
            self._tail = new_node
        new_node.next = self._tail

    def __len__(self):
        length = 0
        current_node = self._head
        if current_node is None:
            return length
        while current_node.next != self._head:
            length += 1
            current_node = current_node.next
        length += 1  # append head
        return length


l = MyCircularLinkedList()
print(len(l))
l.append(1)
print(len(l))
l.append(2)
print(len(l))
l.append(3)
print(len(l))
l.append(4)
print(len(l))
l.append(5)
print(len(l))
l.append(6)
