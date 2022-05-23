#!/usr/bin/env python3
from slidingwindow import SlidingWindow

"""
Time Complexity:  O(N)
Space Complexity: O(1)
"""


def max_sum_subarray(arr, k):
    max_sum = 0

    for window in SlidingWindow(arr, k):
        max_sum = max(max_sum, window)

    return max_sum


def test_ex1():
    i = [2, 1, 5, 1, 3, 2]
    k = 3
    o = 9

    assert max_sum_subarray(i, k) == o


def test_ex2():
    i = [2, 3, 4, 1, 5]
    k = 2
    o = 7

    assert max_sum_subarray(i, k) == o
