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

    # Deserialize prefix notation string into binary tree
    def deserialize(val):
        stack = val.split(" ")
        return Node.build(stack)

    # Build binary tree from prefix notation stack
    def build(stack):
        if stack[0] == "None":
            stack.pop(0)
            return None
        node = Node(stack.pop(0))
        
        if len(stack) == 0: return node
        elif stack[0] == "None": stack.pop(0)
        else: node.left = Node.build(stack)

        if len(stack) == 0: return node
        elif stack[0] == "None": stack.pop(0)
        else: node.right = Node.build(stack)

        return node

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert Node.deserialize(node.serialize()).left.left.val == 'left.left'

print(node.serialize())

print(Node.deserialize(node.serialize()).serialize())

print(Node.deserialize(node.serialize()).left.left.val)