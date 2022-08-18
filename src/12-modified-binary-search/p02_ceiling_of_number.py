"""
Given an array of numbers sorted in an ascending order, find the ceiling of a given number `key`.
The ceiling of the `key` will be the smallest element in the given array greater than or equal to
the `key`.

Write a function to return the index of the ceiling of the `key`. If there isn't any ceiling, return
-1.
"""


def ceiling_of_number(nums, key):
    """
    Time Complexity:  O(logn)
    Space Complexity: O(1)
    """
    # Return early if the array is empty or the key is greater than all the elements.
    if len(nums) < 1 or key > nums[-1]:
        return -1

    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = start + (end - start) // 2

        if nums[middle] == key:
            return middle

        if key < nums[middle]:
            end = middle - 1
        else:
            start = middle + 1

    """
    Why can we just return `start` here? Why is this guaranteed to be the ceiling?
    
    Starting out binary search, there are three possibilities:
    1. The key is smaller than the smallest element, meaning that the ceiling is the first element.
    2. The key is bigger than the greatest element, meaning that there is no ceiling.
    3. The key is ≥ the smallest element and ≤ the greatest element, meaning that the ceiling is a
       number within the range of numbers.

    Zooming into that third case, binary search will zero in on a single number in a final iteration
    where `start` now points to that number. This leads to two cases:
    1. The key is greater than this number (also implying that this number cannot be the last number
       since that case would have already been caught). `start` will increment, moving into the 
       range of numbers rejected for being greater than the key. This means that `start` now holds
       the smallest number greater than the key / the ceiling.
    2. The key is less than this number. By virtue of binary search, this number must be the 
       ceiling. Any previous number cannot be greater than the key because this range is guaranteed
       by binary search to be less than the key.
    """

    return start


def test_ex1():
    nums = [4, 6, 10]
    key = 6
    actual = ceiling_of_number(nums, key)
    expected = 1
    assert actual == expected


def test_ex2():
    nums = [1, 3, 8, 10, 15]
    key = 12
    actual = ceiling_of_number(nums, key)
    expected = 4
    assert actual == expected


def test_ex3():
    nums = [4, 6, 10]
    key = 17
    actual = ceiling_of_number(nums, key)
    expected = -1
    assert actual == expected


def test_ex4():
    nums = [4, 6, 10]
    key = -1
    actual = ceiling_of_number(nums, key)
    expected = 0
    assert actual == expected


def test_ex5():
    nums = [1, 3, 8, 10, 15]
    key = 4
    actual = ceiling_of_number(nums, key)
    expected = 2
    assert actual == expected
