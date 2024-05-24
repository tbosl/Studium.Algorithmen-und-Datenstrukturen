class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()

    def inorder(self):
        if self.left:
            yield from self.left.inorder()
        yield self.data

        if self.right:
            yield from self.right.inorder()

    def preorder(self):
        yield self.data
        if self.left:
            yield from self.left.preorder()
        if self.right:
            yield from self.right.preorder()

    def print_preorder(self):
        print(self.data)
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def post_order(self):
        if self.left:
            yield from self.left.post_order()
        if self.right:
            yield from self.right.post_order()
        yield self.data

    def print_post_order(self):
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()
        print(self.data)


root = Node("F")
root.insert("B")
root.insert("A")
root.insert("D")
root.insert("C")
root.insert("E")
root.insert("G")
root.insert("I")
root.insert("H")
root.print_post_order()
print("_________")

for i in root.post_order():
    print(i)
