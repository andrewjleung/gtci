from heapq import (heappush, heappop)

"""
Given an array of intervals, find the next interval of each interval. In a list of intervals, for an
interval `i` its next interval `j` will have the smallest start greater than or equal to the end of 
`i`.

Write a function to return an array containing indices of the next interval of each input interval.
If there is no next interval of a given interval, return -1. It is given that none of the intervals
have the same start point.
"""


def next_interval(intervals):
    """
    Time Complexity:  O(nlogn)
    Space Complexity: O(n)
    """
    results = [-1 for i in intervals]  # O(n)
    start_min_heap = []
    end_min_heap = []

    # Populate the start and end min heaps.
    for i in range(len(intervals)):  # O(nlogn)
        heappush(start_min_heap, (intervals[i][0], i))
        heappush(end_min_heap, (intervals[i][1], i))

    # Iterate through all the elements in the end min heap and find their next intervals from the
    # start min heap.
    while len(end_min_heap) > 0:
        _, interval_index = heappop(end_min_heap)
        interval = intervals[interval_index]

        # Remove items from the start min heap which can't possibly be next intervals.
        while len(start_min_heap) > 0 and intervals[start_min_heap[0][1]][0] < interval[1]:
            heappop(start_min_heap)

        # The next element in the start min heap is the next interval (or the interval itself) if
        # it is present.
        if len(start_min_heap) > 0:
            # The next interval is not popped here because it could be the next interval for another
            # interval.
            _, next_interval_index = start_min_heap[0]

            # Account for the found next interval being the same as the previous interval. This
            # would only happen if there is an interval with the same start and end values.
            if interval_index == next_interval_index:
                heappop(start_min_heap)
                _, next_interval_index = start_min_heap[0]

            results[interval_index] = next_interval_index

    return results


def test_ex1():
    intervals = [[2, 3], [3, 4], [5, 6]]
    assert next_interval(intervals) == [1, 2, -1]


def test_ex2():
    intervals = [[3, 4], [1, 5], [4, 6]]
    assert next_interval(intervals) == [2, -1, -1]


def test_ex4():
    intervals = [[2, 4], [3, 5], [4, 6], [5, 7]]
    assert next_interval(intervals) == [2, 3, -1, -1]


def test_ex4():
    intervals = [[1, 2], [2, 2], [3, 4]]
    assert next_interval(intervals) == [1, 2, -1]


def test_ex5():
    intervals = [[1, 6], [2, 3], [3, 4]]
    assert next_interval(intervals) == [-1, 2, -1]


def test_ex6():
    intervals = [[3, 4], [5, 6], [2, 3]]
    assert next_interval(intervals) == [1, -1, 0]


def test_ex7():
    intervals = [[1, 3], [2, 3], [3, 6]]
    assert next_interval(intervals) == [2, 2, -1]
