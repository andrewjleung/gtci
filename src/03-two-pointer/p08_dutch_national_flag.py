import math

"""
Given an array containing 0s, 1s, and 2s, sort the array in-place. You should treat numbers of the
array as objects, hence, we can't count 0s, 1s, and 2s to recreate the array.
"""


def dutch_national_flag(arr):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    left, right, i = 0, len(arr) - 1, 0

    while i <= right:
        if arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1


def test_ex1():
    arr = [1, 0, 2, 1, 0]
    o = [0, 0, 1, 1, 2]
    dutch_national_flag(arr)
    assert arr == o


def test_ex2():
    arr = [2, 2, 0, 1, 2, 0]
    o = [0, 0, 1, 2, 2, 2]
    dutch_national_flag(arr)
    assert arr == o
