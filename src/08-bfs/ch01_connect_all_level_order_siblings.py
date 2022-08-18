from src.datastructures.treenode import TreeNode
from collections import deque


def connect_all(root):
    """
    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    if root is None:
        return

    queue = deque()
    queue.append(root)
    previous = None

    while len(queue) > 0:
        level_size = len(queue)

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
    connect_all(root)
    assert root.next == root.left
    assert root.left.next == root.right
    assert root.right.next == root.left.left
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
    connect_all(root)
    assert root.next == root.left
    assert root.left.next == root.right
    assert root.right.next == root.left.left
    assert root.left.left.next == root.right.left
    assert root.right.left.next == root.right.right
