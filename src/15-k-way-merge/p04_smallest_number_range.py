from heapq import (heappush, heappop)
from collections import deque
import math

"""
Given `m` sorted arrays, find the smallest range that includes at least one
number from each of the `m` lists.
"""


def range_size(r):
    return r[1] - r[0]


def smallest_num_range(lists):
    """
    Time Complexity:  O(n log m)
    Space Complexity: O(m)
    """
    # Establish the min heap with the first element of every list.
    min_heap = []
    current_max = -math.inf
    for i in range(len(lists)):  # O(m) iterations
        l = lists[i]
        if len(l) > 0:
            heappush(min_heap, (l[0], l, 0))  # O(log m)
            current_max = max(current_max, l[0])

    range_start = 0
    range_end = math.inf

    while len(min_heap) >= len(lists):  # O(n - m) iterations
        # Pop the next smallest element.
        value, l, i = heappop(min_heap)  # O(log m)

        if current_max - value < range_end - range_start:
            range_start = value
            range_end = current_max

        # The max will never leave the heap. The loop will end before it can be
        # removed, so long as we keep updating it as items go into the heap.

        # Replenish the heap if this array still has more elements.
        if i + 1 < len(l):
            heappush(min_heap, (l[i + 1], l, i + 1))
            current_max = max(current_max, l[i + 1])

    return [range_start, range_end]


def test_ex1():
    l1 = [1, 5, 8]
    l2 = [4, 12]
    l3 = [7, 8, 10]
    #     1  2  1  3  1  3  3   2
    l4 = [1, 4, 5, 7, 8, 8, 10, 12]
    lists = [l1, l2, l3]
    actual = smallest_num_range(lists)
    expected = [4, 7]
    assert actual == expected


def test_ex2():
    l1 = [1, 9]
    l2 = [4, 12]
    l3 = [7, 10, 16]
    lists = [l1, l2, l3]
    actual = smallest_num_range(lists)
    expected = [9, 12]
    assert actual == expected
