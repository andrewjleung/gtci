from src.datastructures.treenode import TreeNode
from collections import deque

"""
Given a binary tree, populate an array to represent the averages of all of its levels.
"""


def average(root):
    """
    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    results = []
    if root is None:
        return results

    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        level_size = len(queue)
        level_sum = 0.0

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        results.append(level_sum / level_size)

    return results


def test_ex1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert average(root) == [1, 2.5, 5.5]


def test_ex2():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert average(root) == [12.0, 4.0, 6.5]
