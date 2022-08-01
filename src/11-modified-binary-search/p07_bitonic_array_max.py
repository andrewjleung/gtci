"""
Find the maximum value in a given Bitonic array. An array is considered bitonic if it is 
monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing
means that for any index `i` in the array `arr[i] != arr[i + 1]`.
"""


def bitonic_max(nums):
    """
    Time Complexity:  O(logn)
    Space Complexity: O(1)
    """
    start = 0
    end = len(nums) - 1

    while start < end:
        middle = start + (end - start) // 2

        if nums[middle] < nums[middle + 1]:
            # If we find that from `middle` the array is increasing, `middle` cannot be the maximum.
            # This means we can safely rule it out.
            start = middle + 1
        else:
            # If we find that from `middle` the array is decreasing, `middle` could be the maximum!
            # This means that we can't rule it out yet, and thus we should keep middle in the range.
            end = middle

    return nums[start]


def test_ex1():
    nums = [1, 3, 8, 12, 4, 2]
    actual = bitonic_max(nums)
    expected = 12
    assert actual == expected


def test_ex2():
    nums = [3, 8, 3, 1]
    actual = bitonic_max(nums)
    expected = 8
    assert actual == expected


def test_ex3():
    nums = [1, 3, 8, 12]
    actual = bitonic_max(nums)
    expected = 12
    assert actual == expected


def test_ex4():
    nums = [10, 9, 8]
    actual = bitonic_max(nums)
    expected = 10
    assert actual == expected


def test_ex5():
    nums = [1, 2]
    actual = bitonic_max(nums)
    expected = 2
    assert actual == expected


def test_ex6():
    nums = [2, 1]
    actual = bitonic_max(nums)
    expected = 2
    assert actual == expected
