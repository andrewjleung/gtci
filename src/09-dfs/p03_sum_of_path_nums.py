from src.datastructures.treenode import TreeNode

"""
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will
represent a number. Find the total sum of all the numbers represented by all paths.
"""


def sum_of_path_nums(root):
    """
    Time Complexity:  O(n)
    Space Complexity: O(n) - the recursive call stack!
    """
    def sum_of_path_nums_help(node, path_sum):
        # Remember. This does not mean a leaf was reached.
        if node is None:
            return 0

        # Calculate the new path sum including this node.
        path_sum = 10 * path_sum + node.val

        # If the node is a leaf, then return the current path sum.
        if node.left is None and node.right is None:
            return path_sum

        # Traverse the sub trees.
        return sum_of_path_nums_help(node.left, path_sum) + sum_of_path_nums_help(node.right, path_sum)

    return sum_of_path_nums_help(root, 0)


def test_ex1():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    assert sum_of_path_nums(root) == 408


def test_ex2():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    assert sum_of_path_nums(root) == 332
