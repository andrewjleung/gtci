from heapq import (heappush, heappop)
from src.datastructures.node import (Node, node, node_eq_array)

"""
Given an array of `k` sorted linked lists, merge them into one sorted list.
"""

def merge_k_sorted_lists(lists):
    """
    Time Complexity:  O(n * log k)
    Space Complexity: O(k)
    """
    min_heap = []

    # Add the head of every non-empty list to the min heap.
    for head in lists: # O(k) iterations
        if head is not None:
            heappush(min_heap, head) # O(log k)

    result_head = None
    result_tail = None
    while len(min_heap) > 0: # O(n - k) iterations
        # Get the smallest node from the heap and add it to the result list.
        node = heappop(min_heap) # O(log k)

        if result_head is None:
            result_head = node
            result_tail = node
        else:
            result_tail.next = node
            result_tail = result_tail.next # Move the cursor!!!

        # If this node has a next, add it to the heap.
        if node.next is not None:
            heappush(min_heap, node.next) # O(log k)

    return result_head



def test_ex1():
    l1 = node([2, 6, 8])
    l2 = node([3, 6, 7])
    l3 = node([1, 3, 4])
    actual = merge_k_sorted_lists([l1, l2, l3])
    expected = [1, 2, 3, 3, 4, 6, 6, 7, 8]
    assert node_eq_array(actual, expected)


def test_ex2():
    l1 = node([5, 8, 9])
    l2 = node([1, 7])
    actual = merge_k_sorted_lists([l1, l2])
    expected = [1, 5, 7, 8, 9]
    assert node_eq_array(actual, expected)
