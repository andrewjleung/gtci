import math

"""
Given an array with positive numbers and a positive target number, find all of its contiguous
subarrays whose product is less than the target number.
"""


def subarray_smaller_product(arr, t):
    """
    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    left = 0
    subarrays = []
    window_product = 1

    for right in range(len(arr)):
        window_product *= arr[right]

        if arr[right] < t:
            subarrays.append([arr[right]])

        while window_product >= t:
            window_product /= arr[left]
            left += 1

        if right - left > 0:
            # slicing is O(k) where k is slice size
            subarrays.append(arr[left:right + 1])

    return subarrays


def test_ex1():
    arr = [2, 5, 3, 10]
    t = 30
    o = [[2], [5], [2, 5], [3], [5, 3], [10]]
    assert subarray_smaller_product(arr, t) == o


def test_ex2():
    arr = [8, 2, 6, 5]
    t = 50
    o = [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]
    assert subarray_smaller_product(arr, t) == o
