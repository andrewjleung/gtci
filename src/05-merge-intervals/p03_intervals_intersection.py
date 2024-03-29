from interval import (Interval, intervals, intervals_eq, overlap)

"""
Given two lists of intervals, find the intersection of theses two lists. Each list consists of 
disjoint intervals sorted on their start time.
"""


def intervals_intersection(arr1, arr2):
    """
    Time Complexity:  O(n + m)
    Space Complexity: O(1)
    """
    intersections = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        interval1, interval2 = arr1[i], arr2[j]

        if overlap(interval1, interval2):
            intersections.append(interval_intersection(arr1[i], arr2[j]))

        if interval1.end == interval2.end:
            # Neither interval can possibly overlap with another interval in the other array since
            # intervals within each individual array are assumed to be non-overlapping. Go to tne
            # next interval in both arrays.
            i += 1
            j += 1
        elif interval1.end < interval2.end:
            # The current interval in the first array cannot possibly overlap with any more
            # intervals from the second since intervals within each individual array are assumed to
            # be non-overlapping. Go to the next interval in the first array.
            i += 1
        else:
            # Converse of the above.
            j += 1

    return intersections


def interval_intersection(interval1, interval2):
    return Interval(max(interval1.start, interval2.start), min(interval1.end, interval2.end))


def test_single_intersections():
    arr1 = intervals([[1, 3], [5, 6], [7, 9]])
    arr2 = intervals([[2, 3], [5, 7]])
    actual = intervals_intersection(arr1, arr2)
    expected = intervals([[2, 3], [5, 6], [7, 7]])
    assert intervals_eq(actual, expected)


def test_multiple_intersections():
    arr1 = intervals([[1, 3], [5, 7], [9, 12]])
    arr2 = intervals([[5, 10]])
    actual = intervals_intersection(arr1, arr2)
    expected = intervals([[5, 7], [9, 10]])
    assert intervals_eq(actual, expected)
