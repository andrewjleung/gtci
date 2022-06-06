"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in
the sorted order.
"""


def square_sorted_array(arr):
    """
    Time Complexity:  O()
    Space Complexity: O()
    """
    left, right = 0, len(arr) - 1
    squares = [0 for x in arr]
    highest_square_idx = len(arr) - 1

    while left <= right:
        left_s = arr[left] * arr[left]
        right_s = arr[right] * arr[right]

        if left_s >= right_s:
            squares[highest_square_idx] = left_s
            left += 1
        else:
            squares[highest_square_idx] = right_s
            right -= 1

        highest_square_idx -= 1

    return squares


def test_ex1():
    arr = [-2, -1, 0, 2, 3]
    o = [0, 1, 4, 4, 9]
    assert square_sorted_array(arr) == o


def test_ex2():
    arr = [-3, -1, 0, 1, 2]
    o = [0, 1, 1, 4, 9]
    assert square_sorted_array(arr) == o
