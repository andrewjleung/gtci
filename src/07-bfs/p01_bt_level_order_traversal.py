from collections import deque
from src.datastructures.treenode import TreeNode

"""
Given an binary tree, populate an array to represent its level-by-level traversal. You should 
populate the values of all nodes of each level from left to right in separate sub
arrays.
"""


def traverse(root):
    results = []

    if root is None:
        return results

    q = deque()
    q.append(root)

    while len(q) > 0:
        """
        Time Complexity:  O(n)
        Space Complexity: O(n)
        """

        # Get level_size.
        level_size = len(q)
        current_level = []

        # Remove `level_size` nodes from the queue, accumulating their results and adding their
        # children to the queue.
        for _ in range(level_size):
            current_node = q.popleft()
            current_level.append(current_node.val)
            if current_node.left is not None:
                q.append(current_node.left)
            if current_node.right is not None:
                q.append(current_node.right)

        # Push the current level sub-array to results.
        results.append(current_level)

    return results


def test_ex1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert traverse(root) == [[1], [2, 3], [4, 5, 6, 7]]


def test_ex2():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert traverse(root) == [[12], [7, 1], [9, 10, 5]]
