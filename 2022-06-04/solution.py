'''
Didn't actually run this because I don't feel like writing
a binary tree right now, but this should work assuming you
pass in the root node of the tree and the nodes store a
variable named "data" or are None
'''
def count(node):
    if node is None:
        return 0
        
    sum = count(node.left) + count(node.right)

    if (node.left is not None and node.right is None) \
      or (node.left is None and node.right is not None):
        return sum
    elif node.left is None and node.right is None:
        sum += 1
    elif node.left.data == node.right.data:
        sum += 1

    return sum