from interval import (Interval, intervals)
import heapq

"""
Given a list of intervals representing the start and end time of `N` meetings, find the minimum
number of rooms required to hold all the meetings.
"""


def min_rooms_quadratic(meetings):
    """
    Time Complexity:  O(n^2)
    Space Complexity: O(1)
    """
    min_start = meetings[0].start
    max_end = meetings[0].end

    for i in range(1, len(meetings)):
        min_start = min(min_start, meetings[i].start)
        max_end = max(max_end, meetings[i].end)

    min_rooms = 1

    for time in range(min_start, max_end):
        rooms = 0
        for i in range(len(meetings)):
            if time >= meetings[i].start and time < meetings[i].end:
                rooms += 1

        min_rooms = max(min_rooms, rooms)

    return min_rooms


def min_rooms(meetings):
    """
    Time Complexity:  O(nlogn)
    Space Complexity: O(n)
    """
    current_min_rooms = 0
    rooms = []

    # Sort meetings by start time.
    meetings.sort(key=lambda a: a.start)

    # Iterate through meetings, adding them to the heap.
    for meeting in meetings:
        # Remove all meetings that are completed.
        while len(rooms) > 0 and meeting.start >= rooms[0].end:
            heapq.heappop(rooms)

        # Add this meeting.
        heapq.heappush(rooms, meeting)

        # Compare the current number of rooms to the current best solution.
        current_min_rooms = max(current_min_rooms, len(rooms))

    return current_min_rooms


def test_ex1():
    meetings = intervals([[1, 4], [2, 5], [7, 9]])
    assert min_rooms(meetings) == 2


def test_ex2():
    meetings = intervals([[6, 7], [2, 4], [8, 12]])
    assert min_rooms(meetings) == 1


def test_ex3():
    meetings = intervals([[1, 4], [2, 3], [3, 6]])
    assert min_rooms(meetings) == 2


def test_ex4():
    meetings = intervals([[4, 5], [2, 3], [2, 4], [3, 5]])
    assert min_rooms(meetings) == 2


def test_ex5():
    meetings = intervals([[1, 4], [2, 3], [3, 5], [1, 3], [3, 4]])
    assert min_rooms(meetings) == 3
