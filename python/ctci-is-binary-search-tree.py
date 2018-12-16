""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

import sys


def checkBST(root):
    return validBST(root)


def validBST(node):
    if emptyNode(node):
        return True
    if not validNode(node):
        return False
    else:
        return validBST(node.left) and validBST(node.right)


def validNode(node):
    return validLeftSubtree(node) and validRightSubtree(node)


def validLeftSubtree(node):
    return node.data > getMax(node.left)


def validRightSubtree(node):
    return node.data < getMin(node.right)


def getMax(node):
    if emptyNode(node):
        return -sys.maxsize - 1
    return max(node.data, getMax(node.left), getMax(node.right))


def getMin(node):
    if emptyNode(node):
        return sys.maxsize
    return min(node.data, getMin(node.left), getMin(node.right))


def emptyNode(node):
    if node is None:
        return True
