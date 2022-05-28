"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to
the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to
the given target.
"""


def pair_with_target_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left, right]

        if curr_sum > target:
            right -= 1
        else:
            left += 1

    return None


def test_ex1():
    arr = [1, 2, 3, 4, 6]
    target = 6
    o = [1, 3]

    assert pair_with_target_sum(arr, target) == o


def test_ex2():
    arr = [2, 5, 9, 11]
    target = 11
    o = [0, 2]

    assert pair_with_target_sum(arr, target) == o
