from heapq import (heappush, heappop, heapify, _siftdown, _siftup)
import math

"""
Given an array of numbers and a number `k`, find the median of all the `k` sized sub-arrays (or windows) of the array.
"""


def sliding_window_median(nums, k):
    """
    Time Complexity:  O(nk) - removing from the heap takes O(k)
    Space Complexity: O(k) - ignoring the output array...
    """
    max_heap = []  # Lower half. For odd `k`, will have the greater half.
    min_heap = []  # Upper half.
    results = []

    window_start = 0

    for window_end in range(len(nums)):  # O(n)
        # Add the value at window_end to the heap.
        if len(max_heap) < 1 or nums[window_end] <= -max_heap[0]:
            heappush(max_heap, -nums[window_end])
        else:
            heappush(min_heap, nums[window_end])

        # Remove the number going out of the window once the window is at the right size.
        if window_end > k - 1:
            if nums[window_start] <= -max_heap[0]:
                heapremove(max_heap, -nums[window_start])  # O(k)
            else:
                heapremove(min_heap, nums[window_start])  # O(k)

            window_start += 1

        # Rebalance the heaps.
        if len(max_heap) > len(min_heap) + 1:
            heappush(min_heap, -heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))

        # Accumulate the median once the window is at the right size.
        if window_end >= k - 1:
            if len(max_heap) != len(min_heap):
                results.append(-max_heap[0])
            else:
                results.append((-max_heap[0] + min_heap[0]) / 2.0)

    return results


def heapremove(heap, element):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    # Find the index of the element.
    i = heap.index(element)  # O(n)

    # Remove the element by moving the last node of the heap into its place.
    # This will violate the heap property, requiring you to re-heapify (not the whole heap however).
    heap[i] = heap[-1]
    del heap[-1]

    # If the element was the last element, no heapification is required.
    # Otherwise, re-heapify the single element.
    if i >= len(heap):
        return

    # `heapify` could be used here, but that algorithm is O(n).
    # Since only a single element needs to be adjusted, this can be done in O(logn).
    _siftup(heap, i)  # O(logn)
    _siftdown(heap, 0, i)  # O(logn)


def test_ex1():
    nums = [1, 2, -1, 3, 5]
    k = 2
    assert sliding_window_median(nums, k) == [1.5, 0.5, 1.0, 4.0]


def test_ex2():
    nums = [1, 2, -1, 3, 5]
    k = 3
    assert sliding_window_median(nums, k) == [1.0, 2.0, 3.0]
