from src.datastructures.treenode import TreeNode
from collections import deque

"""
Given a binary tree, return an array containing nodes in its right view. The right view of a binary
tree is the set of nodes visible when the tree is seen from the right side.
"""


def right_view(root):
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

        for i in range(level_size):
            node = queue.popleft()

            if i == level_size - 1:
                results.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    return results


def test_ex1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert right_view(root) == [1, 3, 7]


def test_ex2():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    assert right_view(root) == [12, 1, 5, 3]
