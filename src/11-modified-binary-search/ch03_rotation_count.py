"""
Given an array of numbers which is sorted in ascending order and is rotated `k` times around a 
pivot, find `k`.

You can assume that the array does not have any duplicates.
"""


def rotation_count(nums):
    """
    Time Complexity:  O(logn)
    Space Complexity: O(1)
    """
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = start + (end - start) // 2

        if middle < end and nums[middle] > nums[middle + 1]:
            return middle + 1

        if middle > start and nums[middle - 1] > nums[middle]:
            return middle

        if nums[start] < nums[middle]:
            start = middle + 1
        else:
            end = middle - 1

    return 0


def test_ex1():
    nums = [10, 15, 1, 3, 8]
    actual = rotation_count(nums)
    expected = 2
    assert actual == expected


def test_ex2():
    nums = [4, 5, 7, 9, 10, -1, 2]
    actual = rotation_count(nums)
    expected = 5
    assert actual == expected


def test_ex3():
    nums = [1, 3, 8, 10]
    actual = rotation_count(nums)
    expected = 0
    assert actual == expected


def test_ex4():
    nums = [15, 1, 3, 8, 10]
    actual = rotation_count(nums)
    expected = 1
    assert actual == expected
