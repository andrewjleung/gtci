"""
We are given an unsorted array containing `n + 1` numbers taken from the range 1 to `n`. The array
has only one duplicate but it can be repeated multiple times. Find that duplicate number without
using any extra space. You are, however, allowed to modify the input array.
"""


def find_duplicate_num(nums):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        if nums[j] == nums[i]:
            if j != i:
                return nums[i]

            i += 1
            continue

        nums[i], nums[j] = nums[j], nums[i]


def test_ex1():
    nums = [1, 4, 4, 3, 2]
    assert find_duplicate_num(nums) == 4


def test_ex2():
    nums = [2, 1, 3, 3, 5, 4]
    assert find_duplicate_num(nums) == 3


def test_ex3():
    nums = [2, 4, 1, 4, 4]
    assert find_duplicate_num(nums) == 4


def test_ex4():
    nums = [3, 4, 1, 4, 4]
    assert find_duplicate_num(nums) == 4
