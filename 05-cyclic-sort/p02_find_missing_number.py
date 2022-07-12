

"""
We are given an array containing `n` distinct numbers taken from the range 0 to `n`. Since the array
has only `n` numbers out of the total `n + 1` numbers, find the missing number.
"""


def find_missing_num(nums):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    i = 0

    while i < len(nums):
        j = nums[i]

        # Ignore the number `n` since we cannot possibly swap it into its place since the array is
        # of length `n`.
        if j == i or j >= len(nums):
            i += 1
            continue

        nums[i], nums[j] = nums[j], nums[i]

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return None


def test_ex1():
    nums = [4, 0, 3, 1]
    assert find_missing_num(nums) == 2


def test_ex2():
    nums = [8, 3, 5, 2, 4, 6, 0, 1]
    assert find_missing_num(nums) == 7
