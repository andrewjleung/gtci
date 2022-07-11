from interval import (intervals, Interval, intervals_eq)

"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only
mutually exclusive intervals.
"""


def merge_intervals(intervals):
    """
    Time Complexity:  O()
    Space Complexity: O()
    """
    if len(intervals) < 2:
        return intervals

    # Sort intervals by starting value.
    intervals.sort(key=lambda a: a.start)

    """
    Upon sorting intervals, it follows that for every two adjacent intervals a and b within
    the array that a.start <= b.start.

    In addition, there are four possible cases:

    1. a and b do not overlap
    2. some part of b overlaps with a
    3. a fully overlaps with b
    4. b fully overlaps a but both have the same start time

    Only cases 2-4 can be merged because they overlap. These can be universally recognized as cases
    where b.start is less than or equal to a.end.

    In each case, merging means taking a.start and then the maximum of a.end and b.end.
    """

    results = []
    """
    We may need to merge multiple consecutive intervals, so we keep track of the start of the
    last non-overlapping interval seen and keep accumulating greater and greater ends so long as
    the consecutive intervals overlap.

    As soon as there is an interval that doesn't overlap, that means this interval is done merging
    and can be added to the results accumulator.

    The current non-overlapping b interval then becomes the next starting point, and the algorithm
    continues onwards.
    """
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        b = intervals[i]

        if b.start <= end:
            end = max(end, b.end)
        else:
            results.append(Interval(start, end))
            start = b.start
            end = b.end

    # The last interval still needs to be added to the results array.
    results.append(Interval(start, end))

    return results


def test_ex1():
    arr = intervals([[1, 4], [2, 5], [7, 9]])
    actual = merge_intervals(arr)
    expected = intervals([[1, 5], [7, 9]])
    assert intervals_eq(actual, expected)


def test_ex2():
    arr = intervals([[6, 7], [2, 4], [5, 9]])
    actual = merge_intervals(arr)
    expected = intervals([[2, 4], [5, 9]])
    assert intervals_eq(actual, expected)


def test_ex3():
    arr = intervals([[1, 4], [2, 6], [3, 5]])
    actual = merge_intervals(arr)
    expected = intervals([[1, 6]])
    assert intervals_eq(actual, expected)
