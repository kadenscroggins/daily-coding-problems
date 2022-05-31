class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self):
        # This function user Preorder Traversal
        print(self.val)

        if isinstance(self.left, Node):
            self.left.serialize()
        elif self.left is None:
            print(self.left)
        else: print(self.left.val)

        if isinstance(self.right, Node):
            self.right.serialize()
        elif self.right is None:
            print(self.right)
        else: print(self.right.val)

    def deserialize(val):
        pass

node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'

node.serialize()