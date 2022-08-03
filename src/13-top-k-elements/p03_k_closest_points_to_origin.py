from src.testutils import contains_same_elements
from math import sqrt
from heapq import (heappush, heappop)
from src.datastructures.point import Point

"""
Given an array of points in a 2D plane, find `k` closest points to the origin.
"""


def k_closest_to_origin(points, k):
    """
    Time Complexity:  O(n * log k)
    Space Complexity: O(k)
    """
    max_heap = []

    # Add `k` elements to the heap.
    for i in range(k):
        heappush(max_heap, points[i])

    # Add the remaining elements so long as they are replacing the point with
    # the greatest distance in the heap.
    for i in range(k, len(points)):
        if points[i].dist_from_origin() < max_heap[0].dist_from_origin():
            heappop(max_heap)
            heappush(max_heap, points[i])

    return max_heap


def test_ex1():
    points = [Point(1, 2), Point(1, 3)]
    k = 1
    actual = k_closest_to_origin(points, k)
    expected = [Point(1, 2)]
    assert contains_same_elements(actual, expected)


def test_ex2():
    points = [Point(1, 3), Point(3, 4), Point(2, -1)]
    k = 2
    actual = k_closest_to_origin(points, k)
    expected = [Point(1, 3), Point(2, -1)]
    assert contains_same_elements(actual, expected)
