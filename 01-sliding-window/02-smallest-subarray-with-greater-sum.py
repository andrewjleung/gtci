#!/usr/bin/env python3
from slidingwindow import SlidingWindow

"""
Given an array of positive numbers and a positive number `S`, find the length of the smallest
contiguous subarray whose sum is is greater than or equal to `S`. Return 0 if no such subarray
exists.
"""


def smallest_subarray_with_greater_sum(arr, s):
    """
    Time Complexity:
    Space Complexity:
    """
    return []


def test_ex1():
    i = [2, 1, 5, 2, 3, 2]
    s = 7
    o = 2

    assert smallest_subarray_with_greater_sum(i, s) == o


def test_ex2():
    i = [2, 1, 5, 2, 8]
    s = 7
    o = 1

    assert smallest_subarray_with_greater_sum(i, s) == o


def test_ex3():
    i = [3, 4, 1, 1, 6]
    s = 8
    o = 3

    assert smallest_subarray_with_greater_sum(i, s) == o
