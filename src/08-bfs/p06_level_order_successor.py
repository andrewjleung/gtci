from src.datastructures.treenode import TreeNode
from collections import deque

"""
Given a binary tree and a node, find the level order successor of the given node in the tree. The
level order successor is the node that appears right after the given node in the level order
traversal.
"""


def successor(root, key):
    """
    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    if root is None:
        return None

    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node.val == key:
                return queue.popleft()

    return None


def test_ex1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert successor(root, 3) == root.left.left


def test_ex2():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert successor(root, 9) == root.right.left


def test_ex3():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert successor(root, 12) == root.left
