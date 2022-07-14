"""
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Note: Positive numbers start from 1.
"""


def find_smallest_missing_pos(nums):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        if nums[i] >= len(nums) or nums[i] < 1 or nums[i] == nums[j]:
            i += 1
            continue

        nums[i], nums[j] = nums[j], nums[i]

    for i in range(len(nums)):
        if nums[i] - 1 != i:
            return i + 1

    return len(nums) + 1


def test_ex1():
    nums = [-3, 1, 5, 4, 2]
    assert find_smallest_missing_pos(nums) == 3


def test_ex2():
    nums = [3, -2, 0, 1, 2]
    assert find_smallest_missing_pos(nums) == 4


def test_ex3():
    nums = [2, 3, 5, 1]
    assert find_smallest_missing_pos(nums) == 4


def test_ex4():
    nums = [33, 37, 5]
    assert find_smallest_missing_pos(nums) == 1


def test_ex5():
    nums = [2, 4, 1, 3, 5]
    assert find_smallest_missing_pos(nums) == 6
