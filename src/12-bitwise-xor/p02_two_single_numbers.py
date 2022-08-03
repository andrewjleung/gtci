from src.testutils import contains_same_elements

"""
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear
only once. Find the two numbers that appear only once.
"""


def two_single_numbers_set(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            num_set.remove(num)
        else:
            num_set.add(num)

    return list(num_set)


def two_single_numbers(nums):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    # Find the XOR of both numbers.
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num

    # Find an arbitrary 1 bit in the XOR of both numbers.
    # This corresponds to a bit which both numbers have different (which they are guaranteed to have
    # by virtue of being different numbers).
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1

    # XOR together all numbers that do have the above found bit and those that don't, which ends up
    # separating both numbers into separate partitions, able to be XOR'd with all the other numbers
    # in their respective partitions separately.
    num1, num2 = 0, 0
    for num in nums:
        if (rightmost_set_bit & num) != 0:  # The bit is set.
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]


def test_ex1():
    nums = [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
    actual = two_single_numbers(nums)
    expected = [4, 6]
    assert contains_same_elements(actual, expected)


def test_ex2():
    nums = [2, 1, 3, 2]
    actual = two_single_numbers(nums)
    expected = [1, 3]
    assert contains_same_elements(actual, expected)
