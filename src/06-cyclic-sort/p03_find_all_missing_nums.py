"""
We are given an unsorted array containing numbers taken from the range 1 to `n`. The array can have
duplicates, which means some numbers will be missing. Find all those missing numbers.
"""


def find_missing_nums(nums):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1) - ignoring the output array for some reason...
    """
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        if nums[j] == nums[i]:
            i += 1
            continue

        nums[i], nums[j] = nums[j], nums[i]

    missing = []

    for i in range(len(nums)):
        if nums[i] - 1 != i:
            missing.append(i + 1)

    return missing


def test_ex1():
    nums = [2, 3, 1, 8, 2, 3, 5, 1]
    assert find_missing_nums(nums) == [4, 6, 7]


def test_ex2():
    nums = [2, 4, 1, 2]
    assert find_missing_nums(nums) == [3]


def test_ex3():
    nums = [2, 3, 2, 1]
    assert find_missing_nums(nums) == [4]
