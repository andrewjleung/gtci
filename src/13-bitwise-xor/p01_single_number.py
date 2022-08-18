"""
In a non-empty array of integers, every number appears twice except for one, find that single 
number.
"""


def single_number(nums):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    x1 = 0

    for num in nums:
        x1 ^= num

    return x1


def test_ex1():
    nums = [1, 4, 2, 1, 3, 2, 3]
    actual = single_number(nums)
    expected = 4
    assert actual == expected


def test_ex2():
    nums = [7, 9, 7]
    actual = single_number(nums)
    expected = 9
    assert actual == expected
