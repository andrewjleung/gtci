"""
We are given an unsorted array containing `n` numbers taken from the range 1 to `n`. The array
originally contained all the numbers from 1 to `n`, but due to a data error, one of the numbers got 
duplicated which also resulted in one number going missing. Find both of these numbers.
"""


def find_corrupt_pair(nums):
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

    for i in range(len(nums)):
        if nums[i] - 1 != i:
            return [nums[i], i + 1]


def test_ex1():
    nums = [3, 1, 2, 5, 2]
    assert find_corrupt_pair(nums) == [2, 4]


def test_ex2():
    nums = [3, 1, 2, 3, 6, 4]
    assert find_corrupt_pair(nums) == [3, 5]
