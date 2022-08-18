from src.testutils import contains_same_elements
from heapq import (heappush, heappop)

"""
Given an unsorted array of numbers, find the `k` largest numbers in it.
"""


def top_k_numbers(nums, k):
    """
    Time Complexity:  O(n * log k)
    Space Complexity: O(k)
    """
    min_heap = []

    # Add `k` elements to the heap.
    for i in range(k):  # `k` iterations
        heappush(min_heap, nums[i])  # O(log k)

    # Only add remaining elements to the heap if they are replacing a smaller
    # element. This way we are always removing small elements in favor of larger
    # elements while retaining `k` elements.
    for i in range(k, len(nums)):  # `n - k` iterations
        if nums[i] > min_heap[0]:
            heappop(min_heap)  # O(log k)
            heappush(min_heap, nums[i])  # O(log k)

    return min_heap


def test_ex1():
    nums = [3, 1, 5, 12, 2, 11]
    k = 3
    actual = top_k_numbers(nums, k)
    expected = [5, 12, 11]
    assert contains_same_elements(actual, expected)


def test_ex2():
    nums = [5, 12, 11, -1, 12]
    k = 3
    actual = top_k_numbers(nums, k)
    expected = [12, 11, 12]
    assert contains_same_elements(actual, expected)
