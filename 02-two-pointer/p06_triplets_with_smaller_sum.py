import math

"""
Given an array of unsorted numbers and a target sum, count all triplets in it such that 
arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to
return the count of such triplets.
"""


def triplet_smaller_sum(arr, t):
    """
    Time Complexity:  O(n^2)
    Space Complexity: O(n) for sorting
    """
    arr.sort()
    num_triplets = 0

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            if arr[i] + arr[left] + arr[right] < t:
                num_triplets += right - left
                left += 1
            else:
                right -= 1

    return num_triplets


def test_ex1():
    arr = [-1, 0, 2, 3]
    t = 3
    o = 2
    assert triplet_smaller_sum(arr, t) == o


def test_ex2():
    arr = [-1, 4, 2, 1, 3]
    t = 5
    o = 4
    assert triplet_smaller_sum(arr, t) == o
