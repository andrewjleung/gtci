from src.datastructures.treenode import TreeNode

"""
Given a binary tree and a number `S`, find all paths in the tree such that the sum of all the node
values of each path equal `S`. Please note that the paths can start or end at any node but all paths
must follow direction from parent to child (top to bottom).
"""


def num_sum_paths(root, s):
    """
    Time Complexity:  O(n^2)
    Space Complexity: O(n)
    """
    def num_sum_paths_help(root, s, path):
        if root is None:
            return 0

        path.append(root.val)
        num_paths = 0
        path_sum = 0

        for i in range(len(path) - 1, -1, -1):
            path_sum += path[i]

            if path_sum == s:
                num_paths += 1

        num_paths += num_sum_paths_help(root.left, s, path)
        num_paths += num_sum_paths_help(root.right, s, path)

        del path[-1]

        return num_paths

    return num_sum_paths_help(root, s, [])


def test_ex1():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    s = 12
    assert num_sum_paths(root, s) == 3


def test_ex2():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    s = 11
    assert num_sum_paths(root, s) == 2
