from heapq import (heappush, heappop)

"""
Given an unsorted array array of numbers, find the Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth
distinct element.
"""


def kth_smallest_number(nums, k):
    """
    Time Complexity:  O(n * log k)
    Space Complexity: O(k)
    """
    max_heap = []

    # Add `k` elements to the max heap.
    for i in range(k):
        heappush(max_heap, -nums[i])

    # Add the remaining elements so long as they are replacing a larger element.
    for i in range(k, len(nums)):
        if nums[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])

    # The max heap now contains the smallest k numbers in the array, the root
    # being the largest of these numbers / the Kth smallest number.
    return -max_heap[0]


def test_ex1():
    nums = [1, 5, 12, 2, 11, 5]
    k = 3
    actual = kth_smallest_number(nums, k)
    expected = 5
    assert actual == expected


def test_ex2():
    nums = [1, 5, 12, 2, 11, 5]
    k = 4
    actual = kth_smallest_number(nums, k)
    expected = 5
    assert actual == expected


def test_ex3():
    nums = [5, 12, 11, -1, 12]
    k = 3
    actual = kth_smallest_number(nums, k)
    expected = 11
    assert actual == expected
