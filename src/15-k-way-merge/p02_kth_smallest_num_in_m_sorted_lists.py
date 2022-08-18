from heapq import (heappush, heappop)

"""
Given `m` sorted arrays, find the `k`'th smallest number among all the arrays.
"""


def kth_smallest(lists, k):
    """
    Time Complexity:  O(m log m + k log m)
    Space Complexity: O(m)
    """
    min_heap = []

    # Add the first element of every array to the heap.
    for i in range(len(lists)):  # O(m) iterations
        l = lists[i]
        if len(l) > 0:
            heappush(min_heap, (l[0], l, 0))  # O(log m)

    # Pop and replace elements from the heap until the k'th element is reached.
    number = None
    count = 1
    while len(min_heap) > 0:  # O(k) iterations
        number, l, i = heappop(min_heap)  # O(log m))
        if count == k:
            break

        if i + 1 < len(l):
            heappush(min_heap, (l[i + 1], l, i + 1))  # O(log m)

        count += 1

    # If fewer then `k` were popped, then `k` was bigger than the total number
    # of elements.
    if count < k:
        return ValueError("k is greater than the total number of elements.")

    if number is None:
        return ValueError("No elements.")

    return number


def test_ex1():
    l1 = [2, 6, 8]
    l2 = [3, 6, 7]
    l3 = [1, 3, 4]
    k = 5
    actual = kth_smallest([l1, l2, l3], k)
    expected = 4
    assert actual == expected


def test_ex2():
    l1 = [5, 8, 9]
    l2 = [1, 7]
    k = 3
    actual = kth_smallest([l1, l2], k)
    expected = 7
    assert actual == expected
