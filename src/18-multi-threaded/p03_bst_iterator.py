from src.datastructures.treenode import TreeNode
from multiprocessing import (Lock, Manager, Process)

"""
Implement an iterator for the in-order traversal of a binary search tree (BST).
That is, given a BST, we need to implement two functions:

1. `bool hasNext()`: Returns `true` if at least one element is left in the
   in-order traversal of the BST.
2. `int next()`: Return the next element in the in-order traversal of the BST.
"""

"""
The intuition of this algorithm is that we could traverse a tree with recursion,
but there is no way to stop the recursion to return each value on demand. 
Instead, we model the recursion with a stack similar to a call stack. In-order
traversal goes left-top-right.
"""


class BSTInOrderIterator:
    def __init__(self, root):
        """
        Space Complexity: O(h) - think of the stack like a call stack
        """
        self.stack = Manager().list()
        self.lock = Lock()
        self.p1 = None
        self.__add_lefts__(root)

    def has_next(self):
        """
        Time Complexity:  O(1)
        """
        # Wait for the `__add_lefts__` process to complete.
        self.__check_process__()
        return len(self.stack) > 0

    def next(self):
        """
        Time Complexity:  O(1) - amortized, `__add_lefts__` only visits each node once.
        """
        # Only a single thread should be able to modify the state of the stack
        # at any given point, so as to avoid reaching a bad state.
        self.lock.acquire()

        # Wait for the `__add_lefts__` process to complete.
        self.__check_process__()

        # Start traversing the popped node's right left sub-trees in a different
        # process, allowing this call to `next` to immediately return with the
        # results. However, any subsequent calls to `next` or `has_next` should
        # wait for this process to finish.
        node = self.stack.pop()
        self.p1 = Process(target=self.__add_lefts__, args=(node.right,))
        self.p1.start()

        self.lock.release()
        return node.val

    # Traverse and push as many left nodes from the given node as possible.
    def __add_lefts__(self, node):
        """
        Time Complexity:  O(n) - amortized, each node only is visited once
        """
        while node is not None:
            self.stack.append(node)
            node = node.left

    # If the process used to traverse left sub-trees after the previous `next`
    # call is still going, wait for it to complete.
    def __check_process__(self):
        if self.p1 is not None and self.p1.is_alive():
            self.p1.join()


def test_ex1():
    root = TreeNode(10)
    root.left = TreeNode(4)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(14)
    root.right.right = TreeNode(19)
    root.right.right.right = TreeNode(20)
    traversal = [1, 4, 10, 14, 15, 19, 20]
    iterator_traversal = []
    iterator = BSTInOrderIterator(root)
    while iterator.has_next():
        iterator_traversal.append(iterator.next())
    assert traversal == iterator_traversal
