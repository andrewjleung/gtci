from heapq import (heappush, heappop)

"""
Given an array, find the sum of all numbers between the k1th and k2th smallest
elements of that array.
"""


def sum_of_elements(nums, k1, k2):
    """
    Time Complexity:  O(n * log k2)
    Space Complexity: O(k2)
    """
    # Edge case, no number in between.
    if k1 == k2 or abs(k2 - k1) == 1:
        return 0

    max_heap = []

    # Assuming `k2` doesn't always need to be greater than `k1`.
    top_k = max(k1, k2)
    bot_k = min(k1, k2)

    # Push `top_k - 1` elements to the heap.
    for i in range(top_k - 1):  # O(top_k - 1) iterations
        heappush(max_heap, -nums[i])  # O(log k2)

    # Push the remaining elements to the heap, so long as they are replacing a
    # larger number. This will get us the `top_k - 1`th smallest numbers in order.
    for i in range(top_k - 1, len(nums)):  # O(n - (top_k - 1)) iterations
        if nums[i] < -max_heap[0]:
            heappop(max_heap)  # O(log k2)
            heappush(max_heap, -nums[i])  # O(log k2)

    sum = 0

    # Until we reach the `bot_k`th element, add elements to sum.
    for _ in range(top_k - bot_k - 1):  # O(k2 - k1) iterations
        sum -= heappop(max_heap)  # O(log k2)

    return sum


def test_ex1():
    nums = [1, 3, 12, 5, 15, 11]
    k1 = 3
    k2 = 6
    actual = sum_of_elements(nums, k1, k2)
    expected = 23
    assert actual == expected


def test_ex2():
    nums = [3, 5, 8, 7]
    k1 = 1
    k2 = 4
    actual = sum_of_elements(nums, k1, k2)
    expected = 12
    assert actual == expected
