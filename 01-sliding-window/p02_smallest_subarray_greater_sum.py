import math

"""
Given an array of positive numbers and a positive number `S`, find the length of the smallest
contiguous subarray whose sum is is greater than or equal to `S`. Return 0 if no such subarray
exists.
"""


def smallest_subarray_sum(arr, s):
    window_start = 0
    window_sum = 0
    min_size = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_size = min(min_size, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    if min_size == math.inf:
        return 0

    return min_size


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
