from slidingwindow import FixedIntegerSlidingWindow
import math

"""
Given an array of positive numbers and a positive number `k`, find the maximum sum of any contiguous
subarray of size `k`.
"""


def max_sum_subarray(arr, k):
    """
    Time Complexity:  O(N)
    Space Complexity: O(1)
    """
    window_start = 0
    curr_sum = 0
    max_sum = 0

    for window_end in range(len(arr)):
        curr_sum += arr[window_end]

        if window_end >= k:
            curr_sum -= arr[window_start]
            window_start += 1

        max_sum = max(max_sum, curr_sum)

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
