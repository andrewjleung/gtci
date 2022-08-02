"""
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary 
number, find if a given `key` is present in it.

Write a function to return the index of a `key` in the rotated array. If the `key` is not present,
return -1. You can assume that the given array does not have any duplicates.
"""


def search_rotated_arr(nums, key):
    """
    Time Complexity:  O(logn)
    Space Complexity: O(1)
    """
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = start + (end - start) // 2

        if nums[middle] == key:
            return middle

        if nums[start] <= nums[middle]:
            # The first half is strictly increasing and the second half contains the circle start.
            if nums[start] <= key and key < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            # The second half is strictly increasing and the first half contains the circle start.
            if nums[middle] < key and key <= nums[end]:
                start = middle + 1
            else:
                end = middle - 1

    return -1


def test_ex1():
    nums = [10, 15, 1, 3, 8]
    key = 15
    actual = search_rotated_arr(nums, key)
    expected = 1
    assert actual == expected


def test_ex2():
    nums = [4, 5, 7, 9, 10, -1, 2]
    key = 10
    actual = search_rotated_arr(nums, key)
    expected = 4
    assert actual == expected
