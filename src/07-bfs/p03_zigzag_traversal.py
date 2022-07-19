from src.datastructures.treenode import TreeNode
from collections import deque

"""
Given a binary tree, populate an array to represent its zigzag level order traversal. You should
populate the values of all nodes of the first level from left to right, then right to left for the
next level and keep alternating in the same manner for the following levels.
"""


def zigzag(root):
    """
    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    results = []

    if root is None:
        return results

    l2r = True
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        level_size = len(queue)
        current_level = deque()

        for _ in range(level_size):
            node = queue.popleft()

            if l2r:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        results.append(list(current_level))
        l2r = not l2r

    return results


def test_ex1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert zigzag(root) == [[1], [3, 2], [4, 5, 6, 7]]


def test_ex2():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    assert zigzag(root) == [[12], [1, 7], [9, 10, 5], [17, 20]]
