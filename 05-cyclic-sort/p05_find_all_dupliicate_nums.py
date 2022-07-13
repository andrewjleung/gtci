"""
We are given an unsorted array containing `n` numbers taken from the range 1 to `n`. The array has
some numbers appearing twice, find all these duplicate numbers using constant space.
"""


def find_all_duplicate_nums(nums):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        if nums[i] == nums[j]:
            i += 1
            continue

        nums[i], nums[j] = nums[j], nums[i]

    duplicates = []

    for i in range(len(nums)):
        if nums[i] - 1 != i:
            duplicates.append(nums[i])

    return duplicates


def test_ex1():
    nums = [3, 4, 4, 5, 5]
    assert find_all_duplicate_nums(nums) == [5, 4]  # Order shouldn't matter.


def test_ex2():
    nums = [5, 4, 7, 2, 3, 5, 3]
    assert find_all_duplicate_nums(nums) == [3, 5]
