"""
Given an array of numbers sorted in ascending order, find the range of a given number `key`. The 
range of the `key` will be the first and last position of the `key` in the array.

Write a function to return the range of the `key`. If the `key` is not present, return [-1, -1].
"""


def number_range(nums, key):
    """
    Time Complexity:  O(logn)
    Space Complexity: O(1)
    """
    result = [-1, -1]

    # Attempt to find the lower bound of the range.
    result[0] = modified_binary_search(nums, key, False)

    # Attempt to find the upper bound of the range if the number was found to exist in the previous
    # search.
    if result[0] != -1:
        result[1] = modified_binary_search(nums, key, True)

    return result


def modified_binary_search(nums, key, find_max):
    key_index = -1
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = start + (end - start) // 2

        if key < nums[middle]:
            end = middle - 1
        elif key > nums[middle]:
            start = middle + 1
        else:
            # `key_index` will always be set to the middle when it is found. Finding the low index
            # of the range means that this `key_index` holds the lowest index in the key's range
            # since you will keep searching the lower range trying to find the key again. The same
            # goes for when searching for the highest index of the key's range.
            key_index = middle
            if find_max:
                start = middle + 1
            else:
                end = middle - 1

    return key_index


def test_ex1():
    nums = [4, 6, 6, 6, 9]
    key = 6
    actual = number_range(nums, key)
    expected = [1, 3]
    assert actual == expected


def test_ex2():
    nums = [1, 3, 8, 10, 15]
    key = 10
    actual = number_range(nums, key)
    expected = [3, 3]
    assert actual == expected


def test_ex3():
    nums = [1, 3, 8, 10, 15]
    key = 12
    actual = number_range(nums, key)
    expected = [-1, -1]
    assert actual == expected


def test_ex4():
    nums = [4, 6, 6, 6, 9]
    key = 3
    actual = number_range(nums, key)
    expected = [-1, -1]
    assert actual == expected
