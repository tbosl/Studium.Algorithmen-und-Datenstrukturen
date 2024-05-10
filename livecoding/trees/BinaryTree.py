class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                # self.left = Node(data) -> not allowed (if left not none!!!!)
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        # self.right = Node(data)
        # no equal check as we assume, that the tree has only unique values
        else:
            self.data = data  # probably nto that common.

    def find_val(self, val):
        if val < self.data:
            if self.left is None:
                return False
            return self.left.find_val(val)
        elif val > self.data:
            if self.right is None:
                return False
            return self.right.find_val(val)
        else:
            return True

    def print(self):  # (in order print)
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()

    def inorder(self):
        if self.left:
            yield from self.left.inorder()  # generator delegation
        yield self.data
        if self.right:
            yield from self.right.inorder()


# root = Node('F')
# root.insert('A')
# root.insert('B')
# root.insert('G')
#
# print(root.left.data)
# print(root.left.right.data)
# print(root.right.data)

root = Node('F')

for v in 'BADCEGIH':  # (just for order like on script
    root.insert(v)
# root.print()

i = iter(root.inorder())
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))

for v in root.inorder():
    print(v)
