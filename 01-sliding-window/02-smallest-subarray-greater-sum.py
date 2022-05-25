#!/usr/bin/env python3
from slidingwindow import IntegerSlidingWindow
import math

"""
Given an array of positive numbers and a positive number `S`, find the length of the smallest
contiguous subarray whose sum is is greater than or equal to `S`. Return 0 if no such subarray
exists.
"""


def smallest_subarray_sum(arr, s):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    if s <= 0:
        raise ValueError("s must be greater than 0")

    w = IntegerSlidingWindow(arr)
    smallest = math.inf

    while not w.is_at_end():
        w.extend_right()

        while (w.window_sum >= s):
            smallest = min(smallest, len(w))
            w.retract_left()

    if smallest == math.inf:
        return 0

    return smallest


def test_ex1():
    i = [2, 1, 5, 2, 3, 2]
    s = 7
    o = 2

    assert smallest_subarray_sum(i, s) == o


def test_ex2():
    i = [2, 1, 5, 2, 8]
    s = 7
    o = 1

    assert smallest_subarray_sum(i, s) == o


def test_ex3():
    i = [3, 4, 1, 1, 6]
    s = 8
    o = 3

    assert smallest_subarray_sum(i, s) == o


def test_ex4():
    i = [1, 2, 3, 4, 5]
    s = 16
    o = 0

    assert smallest_subarray_sum(i, s) == o


def test_ex5():
    i = [1, 3, 1, 2]
    s = 2
    o = 1

    assert smallest_subarray_sum(i, s) == o
