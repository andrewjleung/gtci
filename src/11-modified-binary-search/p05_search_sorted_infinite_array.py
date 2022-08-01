from src.datastructures.arrayreader import ArrayReader

"""
Given an infinite sorted array (or an array with unknown size), find if a given number `key` is
present in the array. Write a function to return the index of the `key` if it is present in the
array, otherwise return -1.

Since it is not possible to define an array with infinite (unknown) size, you will be provided with
an interface `ArrayReader` to read elements of the array. `ArrayReader.get(index)` will return the
number at `index`' if the array's size is smaller than the index, it will return `Integer.MAX_VALUE`.
"""


def search_infinite_arr(nums, key):
    """
    Time Complexity:  O(logn)
    Space Complexity: O(1)
    """
    start = 0
    end = 0

    # Find an `end`` which is greater than `key` by exponentially growing the upper bound.
    while nums.get(end) <= key:
        if nums.get(end) == key:
            return end

        start = end + 1
        end *= 2
        end += 2

    # Binary search this range for the key.
    while start <= end:
        middle = start + (end - start) // 2

        if key == nums.get(middle):
            return middle

        if key < nums.get(middle):
            end = middle - 1
        else:
            start = middle + 1

    return -1


def test_ex1():
    nums = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    key = 16
    actual = search_infinite_arr(nums, key)
    expected = 6
    assert actual == expected


def test_ex2():
    nums = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    key = 11
    actual = search_infinite_arr(nums, key)
    expected = -1
    assert actual == expected


def test_ex3():
    nums = ArrayReader([1, 3, 8, 10, 15])
    key = 15
    actual = search_infinite_arr(nums, key)
    expected = 4
    assert actual == expected


def test_ex4():
    nums = ArrayReader([1, 3, 8, 10, 15])
    key = 200
    actual = search_infinite_arr(nums, key)
    expected = -1
    assert actual == expected
