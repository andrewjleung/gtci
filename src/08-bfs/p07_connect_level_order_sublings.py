from src.datastructures.treenode import TreeNode
from collections import deque

"""
Given a binary tree, connect each node with its level order successor. The last node of each level
should point to a null node.
"""


def connect(root):
    """
    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        level_size = len(queue)
        previous = None

        for _ in range(level_size):
            node = queue.popleft()

            if previous is not None:
                previous.next = node

            previous = node

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


def test_ex1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    connect(root)
    assert root.next is None
    assert root.left.next == root.right
    assert root.right.next is None
    assert root.left.left.next == root.left.right
    assert root.left.right.next == root.right.left
    assert root.right.left.next == root.right.right


def test_ex2():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect(root)
    assert root.next is None
    assert root.left.next == root.right
    assert root.right.next is None
    assert root.left.left.next == root.right.left
    assert root.right.left.next == root.right.right
