import math

"""
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as
close to the target number as possible, return the sum of the triplet. If there are more than one
such triplet, return the sum of the triplet with the smallest sum.
"""


def triplet_sum_close_to_target(arr, t):
    """
    Time Complexity:  O(n^2)
    Space Complexity: O(n) for sorting
    """
    arr.sort()  # O(n * Log n) TimSort
    smallest_diff = math.inf

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while (left < right):
            target_diff = t - arr[i] - arr[left] - arr[right]

            if target_diff == 0:
                return t

            if abs(target_diff) < abs(smallest_diff) or (abs(
                    target_diff) == abs(smallest_diff) and target_diff > smallest_diff):
                smallest_diff = target_diff

            if target_diff > 0:
                left += 1
            else:
                right -= 1

    return t - smallest_diff


def test_ex1():
    arr = [-2, 0, 1, 2]
    t = 2
    o = 1
    assert triplet_sum_close_to_target(arr, t) == o


def test_ex2():
    arr = [-3, -1, 1, 2]
    t = 1
    o = 0
    assert triplet_sum_close_to_target(arr, t) == o


def test_ex3():
    arr = [1, 0, 1, 1]
    t = 100
    o = 3
    assert triplet_sum_close_to_target(arr, t) == o
