from src.datastructures.treenode import TreeNode
from collections import deque

"""
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest
path from the root node to the nearest leaf node.
"""


def min_depth(root):
    """
    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    depth = 0
    if root is None:
        return depth

    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        depth += 1
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            if node.left is None and node.right is None:
                return depth

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    return depth


def test_ex1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert min_depth(root) == 2


def test_ex2():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert min_depth(root) == 2


def test_ex3():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(11)
    assert min_depth(root) == 3
