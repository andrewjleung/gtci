from src.datastructures.treenode import TreeNode

"""
Given a binary tree and a number `S`, find all paths from root-to-leaf such that the sum of all the 
node values of each path equals `S`.
"""


def all_sum_paths(root, s):
    """
    Time Complexity:  O(nlogn) - O(n) calls on the stack, O(nlogn) time to copy at most O(n) paths.
    Space Complexity: O(nlogn)
    """
    # The potential number of paths stored is O(n). Each path can contain at most O(logn) elements.
    # This gives us a space complexity of
    results = []

    def all_sum_paths_help(node, s, path):
        if node is None:
            return

        # Use the same path list for all recursion. This way we don't have to keep making new lists.
        path.append(node.val)

        if node.val == s and node.left is None and node.right is None:
            # Copying the list is O(logn) (the max path length).
            results.append(list(path))
        else:
            s = s - node.val
            all_sum_paths_help(node.left, s, path)
            all_sum_paths_help(node.right, s, path)

        # Delete the current node from the path list to backtrack/going back up the call stack.
        del path[-1]

    # O(n) space for the call stack.
    all_sum_paths_help(root, s, [])
    return results


def test_exists1():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)
    s = 12
    assert all_sum_paths(root, s) == [[1, 7, 4], [1, 9, 2]]


def test_exists2():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    s = 23
    assert all_sum_paths(root, s) == [[12, 7, 4], [12, 1, 10]]
