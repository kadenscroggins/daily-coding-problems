class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Serialize binary tree into string using preorder traversal
    def serialize(self):
        ret = str(self.val)

        if isinstance(self.left, Node):
            ret += " " + self.left.serialize()
        elif self.left is None:
            ret += " None"
        else: ret += " " + str(self.left.val)

        if isinstance(self.right, Node):
            ret += " " + self.right.serialize()
        elif self.right is None:
            ret += " None"
        else: ret += " " + str(self.right.val)

        return ret

    # Deserialize string into binary tree using preorder traversal
    def deserialize(val):
        pass

node = Node(1, Node(2, Node(4)), Node(3))
#assert deserialize(serialize(node)).left.left.val == 'left.left'

print(node.serialize())