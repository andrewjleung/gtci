"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole 
array.
"""


def min_window_sort(arr):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    low = 0
    high = len(arr) - 1

    while low < len(arr) - 1 and arr[low] < arr[low + 1]:
        low += 1

    if low >= len(arr) - 1:
        return 0

    while high > 0 and arr[high - 1] < arr[high]:
        high -= 1

    window_max = max(arr[low:high + 1])
    window_min = min(arr[low:high + 1])

    while low > 0 and arr[low - 1] > min_window:
        low -= 1

    while high < len(arr) - 1 and arr[high + 1] < window_max:
        high += 1

    return high - low + 1


def test_ex1():
    arr = [1, 2, 5, 3, 7, 10, 9, 12]
    o = 5
    assert min_window_sort(arr) == o


def test_ex2():
    arr = [1, 3, 2, 0, -1, 7, 10]
    o = 5
    assert min_window_sort(arr) == o


def test_ex3():
    arr = [1, 2, 3]
    o = 0
    assert min_window_sort(arr) == o


def test_ex4():
    arr = [3, 2, 1]
    o = 3
    assert min_window_sort(arr) == o
