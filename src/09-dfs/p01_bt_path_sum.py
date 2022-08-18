from src.datastructures.treenode import TreeNode

"""
Given a binary tree and a number `S`, find if the tree has a path from root to leaf such that the sum of all the node values of that path equals `S`.
"""


def path_sum(root, s):
    """
    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    # None case.
    if root is None:
        return False

    # Leaf case.
    if root.left is None and root.right is None:
        return root.val == s

    # Non-leaf case.
    s = s - root.val
    return path_sum(root.left, s) or path_sum(root.right, s)


def test_exists1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    s = 10
    assert path_sum(root, s)


def test_exists2():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    s = 23
    assert path_sum(root, s)


def test_not_exists():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    s = 16
    assert not path_sum(root, s)
