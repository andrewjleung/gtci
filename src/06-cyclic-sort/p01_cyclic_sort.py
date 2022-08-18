"""
We are given an array containing `n` objects. Each object, when created, was assigned a unique
number from range 1 to `n` based on their creation sequence. This means that the object with 
sequence number 3 was created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation sequence number in O(n) and without
using any extra space. For simplicity, let's assume we are passed an integer array containing only
the sequence numbers, though each number is actually an object.
"""


def cyclic_sort(arr):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    i = 0

    while i < len(arr):
        j = arr[i] - 1

        if j == i:
            i += 1
            continue

        arr[j], arr[i] = arr[i], arr[j]


def test_ex1():
    arr = [3, 1, 5, 4, 2]
    o = [1, 2, 3, 4, 5]
    cyclic_sort(arr)
    assert arr == o


def test_ex2():
    arr = [2, 6, 4, 3, 1, 5]
    o = [1, 2, 3, 4, 5, 6]
    cyclic_sort(arr)
    assert arr == o


def test_ex3():
    arr = [1, 5, 6, 4, 3, 2]
    o = [1, 2, 3, 4, 5, 6]
    cyclic_sort(arr)
    assert arr == o
