from src.datastructures.treenode import TreeNode
from multiprocessing import Process, cpu_count, Manager

"""
Given the root of a binary tree, invert it.
"""


class Invert:
    def invert(self, root):
        """
        Time Complexity:  O(n)
        Space Complexity: O(h)
        """
        # TODO: This does not currently work because each process has its own
        #       copy of `root`. In order to share a common root, you'd have to
        #       either redefine the given binary tree in terms of a proxy object
        #       like `multiprocessing.Manager.list` so that updates across all
        #       processes can be tracked. Alternatively, make some sort of proxy
        #       implementation for a binary tree.
        num_cpus = cpu_count()
        return self.invert_multiprocessed(root, num_cpus)

    def invert_multiprocessed(self, root, num_cpus):
        if root is None:
            return root

        root.left, root.right = root.right, root.left

        if num_cpus > 0:
            p = Process(target=self.invert_multiprocessed,
                        args=(root.left, num_cpus / 2))
            p.start()
            self.invert_multiprocessed(root.right, num_cpus / 2)
            p.join()
        else:
            self.invert_multiprocessed(root.left, 0)
            self.invert_multiprocessed(root.right, 0)

        return root


def invert(root):
    """
    Time Complexity:  O(n)
    Space Complexity: O(h)
    """
    if root is None:
        return root

    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)

    return root


def test_ex1():
    root = TreeNode(10)
    root.left = TreeNode(4)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(14)
    root.right.right = TreeNode(19)
    root.right.right.left = TreeNode(20)
    inverted = TreeNode(10)
    inverted.right = TreeNode(4)
    inverted.left = TreeNode(15)
    inverted.right.right = TreeNode(1)
    inverted.left.right = TreeNode(14)
    inverted.left.left = TreeNode(19)
    inverted.left.left.right = TreeNode(20)
    invert(root)
    assert root == inverted
