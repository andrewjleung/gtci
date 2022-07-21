from src.datastructures.treenode import TreeNode

"""
Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes
on the longest path between any two leaf nodes. The diameter of a tree may or may not pass through
the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.
"""


class TreeDiameter:
    """
    Time Complexity:  O(n)
    Space Complexity: O(n)
    """

    def __init__(self):
        self.max_diameter = 0

    def get_max_diameter(self, root):
        self.calculate_height(root)
        return self.max_diameter

    def calculate_height(self, root):
        if root is None:
            return 0

        left_max_height = self.calculate_height(root.left)
        right_max_height = self.calculate_height(root.right)

        if left_max_height > 0 and right_max_height > 0:
            diameter = 1 + left_max_height + right_max_height

            self.max_diameter = max(self.max_diameter, diameter)

        return 1 + max(left_max_height, right_max_height)


def test_ex1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    td = TreeDiameter()
    assert td.get_max_diameter(root) == 5


def test_ex2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.right = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    td = TreeDiameter()
    assert td.get_max_diameter(root) == 7
