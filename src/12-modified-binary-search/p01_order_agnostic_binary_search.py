"""
Given a sorted array of numbers, find if a given number `key` is present in the array. Though we 
know that the array is sorted, we don't know if it's sorted in ascending or descending order. You
should assume that the array can have duplicates.

Write a function to return the index of the `key` if it is present in the array, otherwise return 
-1.
"""


def order_agnostic_binary_search(nums, key):
    """
    Time Complexity:  O(logn)
    Space Complexity: O(1)
    """
    # An empty array can't possibly contain the key.
    if len(nums) < 1:
        return -1

    start = 0
    end = len(nums) - 1

    # Determine the sort order.
    asc = True
    if nums[start] > nums[end]:
        asc = False

    # Do a binary search.
    while start <= end:
        middle = start + int((end - start) / 2)

        if nums[middle] == key:
            return middle

        # Determine the half to search depending on whether the list is ascending or not.
        if (asc and key < nums[middle]) or (not asc and key > nums[middle]):
            end = middle - 1
        else:
            start = middle + 1

    return -1


def test_ex1():
    nums = [4, 6, 10]
    key = 10
    actual = order_agnostic_binary_search(nums, key)
    expected = 2
    assert actual == expected


def test_ex2():
    nums = [1, 2, 3, 4, 5, 6, 7]
    key = 5
    actual = order_agnostic_binary_search(nums, key)
    expected = 4
    assert actual == expected


def test_ex3():
    nums = [10, 6, 4]
    key = 10
    actual = order_agnostic_binary_search(nums, key)
    expected = 0
    assert actual == expected


def test_ex4():
    nums = [10, 6, 4]
    key = 4
    actual = order_agnostic_binary_search(nums, key)
    expected = 2
    assert actual == expected


def test_ex5():
    nums = [10, 6, 4]
    key = 3
    actual = order_agnostic_binary_search(nums, key)
    expected = -1
    assert actual == expected


def test_ex6():
    nums = []
    key = 3
    actual = order_agnostic_binary_search(nums, key)
    expected = -1
    assert actual == expected
