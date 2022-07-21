from src.datastructures.treenode import TreeNode
import math

"""
Find the path with the maximum sum in a given binary tree. Write a function that returns the 
maximum sum.

A path can be defined as a sequence of nodes between any two nodes and doesn't necessarily pass 
through the root. The path must contain at least one node.
"""


class MaxPathSum:
    """
    Time Complexity:  O(n)
    Space Complexity: O(n)
    """

    def __init__(self):
        self.max_path_sum = -math.inf

    def max_sum(self, node):
        """
        Returns the sum of the max straight path going down a single direction starting at the given node.
        """
        if node is None:
            return 0

        left_max_sum = self.max_sum(node.left)
        right_max_sum = self.max_sum(node.right)

        # Paths can have negative sums! Ignore them.
        left_max_sum = max(left_max_sum, 0)
        right_max_sum = max(right_max_sum, 0)

        # At the same time, determine the max path sum.
        """ 
        There are three situations:
        1.  If there are two children, the max path sum from this node is the max straight sum of the
            left and right trees added to this node's value.
        2.  If there is only one child, the other child's max straight sum will be zero and the max
            path sum from this node is this node's value plus the max straight sum of the child.
        3.  If there are no children, then the value of the path (debatably a path) is the node.
        """
        path_sum = node.val + left_max_sum + right_max_sum
        self.max_path_sum = max(self.max_path_sum, path_sum)

        return node.val + max(left_max_sum, right_max_sum)

    def get_max_path_sum(self, node):
        self.max_sum(node)
        return self.max_path_sum


def test_ex1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    assert MaxPathSum().get_max_path_sum(root) == 16


def test_ex2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.right = TreeNode(9)
    assert MaxPathSum().get_max_path_sum(root) == 31
