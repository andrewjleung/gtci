"""
Given an array of sorted numbers, separate all duplicates from it in-place. You should not use any
extra space; move all duplicates at the end of the array and after moving return the length of the
subarray that has no duplicate in it
"""


def separate_duplicates(arr):
    """
    Time Complexity:  O()
    Space Complexity: O()
    """
    pass


def test_ex1():
    arr = [2, 3, 3, 3, 6, 9, 9]
    o = 4
    assert separate_duplicates(arr) == o


def test_ex2():
    arr = [2, 2, 2, 11]
    o = 2
    assert separate_duplicates(arr) == o
