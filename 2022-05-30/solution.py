class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self):
        # This function user Preorder Traversal

        ret = str(self.val) + " "

        if isinstance(self.left, Node):
            ret += self.left.serialize()
        elif self.left is None:
            ret += "None "
        else: ret += str(self.left.val) + " "

        if isinstance(self.right, Node):
            ret += self.right.serialize()
        elif self.right is None:
            ret += "None "
        else: ret += str(self.right.val) + " "

        return ret

    def deserialize(val):
        pass

node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'

print(node.serialize())