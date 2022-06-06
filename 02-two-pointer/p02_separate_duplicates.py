"""
Given an array of sorted numbers, separate all duplicates from it in-place. You should not use any
extra space; move all duplicates at the end of the array and after moving return the length of the
subarray that has no duplicate in it
"""


def separate_duplicates(arr):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    next_non_duplicate, i = 1, 0

    while i < len(arr):
        if arr[i] != arr[next_non_duplicate - 1]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


def test_ex1():
    arr = [2, 3, 3, 3, 6, 9, 9]
    o = 4
    assert separate_duplicates(arr) == o


def test_ex2():
    arr = [2, 2, 2, 11]
    o = 2
    assert separate_duplicates(arr) == o
