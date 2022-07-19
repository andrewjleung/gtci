from src.datastructures.treenode import TreeNode
from collections import deque

"""
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order,
i.e., the lowest level comes first. You should populate the values of all nodes in each level from
left to right in separate sub-arrays.
"""


def rtraverse(root):
    results = deque()

    if root is None:
        return results

    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        results.appendleft(current_level)

    return list(results)


def test_ex1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert rtraverse(root) == [[4, 5, 6, 7], [2, 3], [1]]


def test_ex2():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert rtraverse(root) == [[9, 10, 5], [7, 1], [12]]
