"""
Given a bitonic array, find if the given `key` is present in it. An array is considered bitonic if
it is monotonically increasing and then monotonically decreasing. Monotonically increasing or
decreasing means that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the `key`. If the 'key' appears more than once, return the
smaller index. If the `key` is not present, return -1.
"""


def max_bitonic(nums):
    """
    Time Complexity:  O(logn)
    Space Complexity: O(1)
    """
    start = 0
    end = len(nums) - 1

    while start < end:
        middle = start + (end - start) // 2

        if nums[middle] < nums[middle + 1]:
            start = middle + 1
        else:
            end = middle

    return start


def binary_search(nums, key, start, end, increasing):
    """
    Time Complexity:  O(logn)
    Space Complexity: O(1)
    """
    print(nums[start:end + 1])
    while start <= end:
        middle = start + (end - start) // 2

        if nums[middle] == key:
            return middle

        if (key < nums[middle] and increasing) or (key > nums[middle] and not increasing):
            end = middle - 1
        else:
            start = middle + 1

    return -1


def bitonic_search(nums, key):
    """
    Time Complexity:  O(logn)
    Space Complexity: O(1)
    """
    start = 0
    end = len(nums) - 1

    # Find the max element / the switching point.
    max_element_index = max_bitonic(nums)

    if nums[max_element_index] == key:
        return max_element_index

    # Search the increasing half.
    index = binary_search(nums, key, 0, max_element_index - 1, True)

    if index != -1:
        return index

    # Search the decreasing half.
    return binary_search(nums, key, max_element_index + 1, end, False)


def test_ex1():
    nums = [1, 3, 8, 4, 3]
    key = 4
    actual = bitonic_search(nums, key)
    expected = 3
    assert actual == expected


def test_ex2():
    nums = [3, 8, 3, 1]
    key = 8
    actual = bitonic_search(nums, key)
    expected = 1
    assert actual == expected


def test_ex3():
    nums = [1, 3, 8, 12]
    key = 12
    actual = bitonic_search(nums, key)
    expected = 3
    assert actual == expected


def test_ex4():
    nums = [10, 9, 8]
    key = 10
    actual = bitonic_search(nums, key)
    expected = 0
    assert actual == expected


def test_ex5():
    nums = [1, 3, 9, 3, 1]
    key = 3
    actual = bitonic_search(nums, key)
    expected = 1
    assert actual == expected
