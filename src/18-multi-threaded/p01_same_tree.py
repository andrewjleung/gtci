from src.datastructures.treenode import TreeNode
from multiprocessing import Process, Value, cpu_count
from ctypes import c_bool
import os

"""
Given the roots of two binary trees `p` and `q`, write a function to check if 
they are the same or not.

Two binary trees are considered the same if they met the following two 
conditions:
1. Both trees are structurally identical.
2. Each corresponding node on both the trees have the same value.
"""


class SameTree:
    def same_tree(self, root1, root2):
        """
        Time Complexity:  O(min(n, m)) - whichever tree has fewer nodes
        Space Complexity: O(min(h1, h2)) - whichever tree is shorter
        """
        self.is_same = Value(c_bool, True)
        # NOTE: `cpu_count` does NOT give you the number of available CPUs, but
        #       rather the total number of CPUs. I could not find a standard way
        #       to find this information on MacOS. This serves as an example for
        #       what to do with this information.
        num_cpus = cpu_count()
        return self.same_tree_multiprocessed(root1, root2, num_cpus)

    def check_right(self, root1, root2, num_cpus):
        result = self.same_tree_multiprocessed(
            root1.right, root2.right, num_cpus / 2)

        # A lock is required since `&=` requires both a read and a write.
        # See the following docs on `multiprocessing.Value`:
        # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Value
        with self.is_same.get_lock():
            self.is_same.value &= result

    def same_tree_multiprocessed(self, root1, root2, num_cpus):
        if root1 is None:
            return root2 is None

        if root2 is None:
            return root1 is None

        if root1.val != root2.val:
            return False

        # If there are more CPUs, check the right sub-tree in another process.
        if num_cpus > 0:
            # TODO: Why do we divide by 2 here?
            p = Process(target=self.check_right,
                        args=(root1, root2, num_cpus / 2))
            p.start()

            result = self.same_tree_multiprocessed(
                root1.left, root2.left, num_cpus / 2)

            with self.is_same.get_lock():
                self.is_same.value &= result

            p.join()
        # If there are no available CPUs, do the work in this current process.
        else:
            result = self.same_tree_multiprocessed(root1.left, root2.left, 0)  \
                and self.same_tree_multiprocessed(root1.right, root2.right, 0)

            with self.is_same.get_lock():
                self.is_same.value &= result

        return self.is_same.value


def same_tree(root1, root2):
    """
    Time Complexity:  O(min(n, m)) - whichever tree has fewer nodes
    Space Complexity: O(min(h1, h2)) - whichever tree is shorter
    """
    if root1 is None:
        return root2 is None

    if root2 is None:
        return root1 is None

    return root1.val == root2.val \
        and same_tree(root1.left, root2.left) \
        and same_tree(root1.right, root2.right)


def test_ex1():
    root1 = TreeNode(10)
    root1.left = TreeNode(4)
    root1.right = TreeNode(15)
    root1.left.left = TreeNode(1)
    root1.right.left = TreeNode(14)
    root2 = TreeNode(10)
    root2.left = TreeNode(4)
    root2.right = TreeNode(15)
    root2.left.left = TreeNode(1)
    root2.right.left = TreeNode(14)
    assert SameTree().same_tree(root1, root2)


def test_ex2():
    root1 = TreeNode(10)
    root1.left = TreeNode(4)
    root1.right = TreeNode(15)
    root1.left.left = TreeNode(1)
    root1.right.left = TreeNode(14)
    root2 = TreeNode(10)
    root2.left = TreeNode(4)
    root2.right = TreeNode(15)
    root2.left.left = TreeNode(1)
    root2.right.left = TreeNode(14)
    root2.right.right = TreeNode(20)
    assert not SameTree().same_tree(root1, root2)


def test_ex2():
    root1 = TreeNode(10)
    root1.left = TreeNode(4)
    root1.right = TreeNode(15)
    root1.left.left = TreeNode(1)
    root1.right.left = TreeNode(14)
    root1.right.right = TreeNode(20)
    root2 = TreeNode(10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(15)
    root2.left.left = TreeNode(1)
    root2.right.left = TreeNode(14)
    root2.right.right = TreeNode(20)
    assert not SameTree().same_tree(root1, root2)
