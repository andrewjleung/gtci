"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole 
array.
"""


def min_window_sort(arr):
    """
    Time Complexity:  O(n*logn)
    Space Complexity: O(n)
    """
    sorted_arr = sorted(arr)
    min_window = 0

    for left in range(len(arr)):
        if arr[left] != sorted_arr[left]:
            min_window -= left
            break

    for right in range(len(arr) - 1, -1, -1):
        if arr[right] != sorted_arr[right]:
            min_window += right + 1
            break

    return min_window


def test_ex1():
    arr = [1, 2, 5, 3, 7, 10, 9, 12]
    sorted_arr = [1, 2, 3, 5, 7, 9, 10, 12]
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
