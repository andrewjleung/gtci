from interval import (Interval, intervals, intervals_eq)
from p01_merge_intervals import merge_intervals

"""
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the
correct position and merge all necessary intervals to produce a list that has only mutually 
exclusive intervals.
"""


def insert_interval(intervals, new_interval):
    """
    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    merged = []
    i = 0

    # Skip/accumulate intervals that come before and don't overlap with the new interval.
    while i < len(intervals) and intervals[i].end < new_interval.start:
        merged.append(intervals[i])
        i += 1

    # Merge all intervals that overlap with the new interval.
    while i < len(intervals) and intervals[i].start <= new_interval.end:
        new_interval.start = min(new_interval.start, intervals[i].start)
        new_interval.end = max(new_interval.end, intervals[i].end)
        i += 1

    merged.append(new_interval)

    # Add the remaining intervals which didn't overlap with the new interval.
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged


def test_ex1():
    arr = intervals([[1, 3], [5, 7], [8, 12]])
    new = Interval(4, 6)
    actual = insert_interval(arr, new)
    expected = intervals([[1, 3], [4, 7], [8, 12]])
    assert intervals_eq(actual, expected)


def test_ex2():
    arr = intervals([[1, 3], [5, 7], [8, 12]])
    new = Interval(4, 10)
    actual = insert_interval(arr, new)
    expected = intervals([[1, 3], [4, 12]])
    assert intervals_eq(actual, expected)


def test_ex3():
    arr = intervals([[2, 3], [5, 7]])
    new = Interval(1, 4)
    actual = insert_interval(arr, new)
    expected = intervals([[1, 4], [5, 7]])
    assert intervals_eq(actual, expected)
