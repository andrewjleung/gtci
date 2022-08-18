from src.datastructures.treenode import TreeNode
from src.testutils import contains_same_elements

"""
Given a number `n`, write a function to return all structurally unique Binary Search Trees (BST) 
that can store values 1 to `n`.
"""

"""
Time Complexity:  O(n * cat(n))
Space Complexity: O(n * cat(n))
"""


def unique_bsts_range(start, end):
    if start > end:
        raise ValueError(
            "Invalid range. Start must be less than or equal to end.")

    if start == end:
        return [TreeNode(start)]

    bsts = []

    for root in range(start, end + 1):
        left_bsts, right_bsts = [None], [None]

        if root != start:
            left_bsts = unique_bsts_range(start, root - 1)

        if root != end:
            right_bsts = unique_bsts_range(root + 1, end)

        for left_bst in left_bsts:
            for right_bst in right_bsts:
                new_bst = TreeNode(root)
                new_bst.left = left_bst
                new_bst.right = right_bst
                bsts.append(new_bst)

    return bsts


def unique_bsts(n):
    return unique_bsts_range(1, n)


def test_ex1():
    n = 2
    actual = unique_bsts(n)

    tree1 = TreeNode(1)
    tree1.right = TreeNode(2)

    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)

    expected = [tree1, tree2]
    assert contains_same_elements(actual, expected)


def test_ex2():
    n = 3
    actual = unique_bsts(n)

    tree1 = TreeNode(1)
    tree1.right = TreeNode(2)
    tree1.right.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.right.left = TreeNode(2)

    tree3 = TreeNode(2)
    tree3.left = TreeNode(1)
    tree3.right = TreeNode(3)

    tree4 = TreeNode(3)
    tree4.left = TreeNode(1)
    tree4.left.right = TreeNode(2)

    tree5 = TreeNode(3)
    tree5.left = TreeNode(2)
    tree5.left.left = TreeNode(1)

    expected = [tree1, tree2, tree3, tree4, tree5]
    assert contains_same_elements(actual, expected)
