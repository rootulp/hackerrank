def isLeaf(node):
    return node.left is None and node.right is None


def height(node):
    if node is None or isLeaf(node):
        return 0
    else:
        return 1 + max(height(node.left), height(node.right))
