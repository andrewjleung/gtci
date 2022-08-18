"""
Given an array of numbers sorted in ascending order, find the element in the array that has the 
minimum difference with the give `key`.
"""


def min_difference_element(nums, key):
    """
    Time Complexity:  O(logn)
    Space Complexity: O(1)
    """
    start = 0
    end = len(nums) - 1

    # Check edge cases where the key comes before/after the range of `nums`.
    if key >= nums[end]:
        return nums[end]

    if key <= nums[start]:
        return nums[start]

    # Binary search for the key.
    while start <= end:
        middle = start + (end - start) // 2

        if nums[middle] == key:
            return key

        if key < nums[middle]:
            end = middle - 1
        else:
            start = middle + 1

    # After the binary search if the key wasn't found, `end` holds the index of the number that
    # would come right before the key while `start` holds the index of the number that would come
    # right after key (after accounting for edge cases). Compare there distances from the key.
    if nums[start] - key < key - nums[end]:
        return nums[start]

    return nums[end]


def test_ex1():
    nums = [4, 6, 10]
    key = 7
    actual = min_difference_element(nums, key)
    expected = 6
    assert actual == expected


def test_ex2():
    nums = [4, 6, 10]
    key = 4
    actual = min_difference_element(nums, key)
    expected = 4
    assert actual == expected


def test_ex3():
    nums = [1, 3, 8, 10, 15]
    key = 12
    actual = min_difference_element(nums, key)
    expected = 10
    assert actual == expected


def test_ex4():
    nums = [4, 6, 10]
    key = 17
    actual = min_difference_element(nums, key)
    expected = 10
    assert actual == expected


def test_ex5():
    nums = [4, 6, 10]
    key = 3
    actual = min_difference_element(nums, key)
    expected = 4
    assert actual == expected
