from src.datastructures.treenode import TreeNode

"""
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
"""


def has_path_with_seq(root, seq):
    """
    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    if not root:
        return len(seq) == 0

    def has_path_with_seq_help(root, seq, level):
        if root is None:
            return False

        # Return early since the current path is longer than the sequence (we're looking for root to
        # leaf paths) or the current node is not equal to its position in the sequence, we know that
        # searching this path can no longer find the correct path.
        if level > len(seq) or seq[level] != root.val:
            return False

        if root.left is None and root.right is None:
            # We would have returned early already if this leaf node didn't equal its correct
            # position. The only thing left to check is that there's nothing more in the sequence.
            return level == len(seq) - 1

        return has_path_with_seq_help(root.left, seq, level + 1) or has_path_with_seq_help(root.right, seq, level + 1)

    return has_path_with_seq_help(root, seq, 0)


def test_ex1():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    assert has_path_with_seq(root, [1, 9, 9])


def test_ex2():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    assert not has_path_with_seq(root, [1, 0, 7])
    assert has_path_with_seq(root, [1, 1, 6])
