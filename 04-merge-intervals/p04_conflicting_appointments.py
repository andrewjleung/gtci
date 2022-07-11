from interval import (Interval, intervals, overlap)

"""
Given an array of intervals representing `N` appointments, find out if a person can attend all the
appointments.
"""


def can_attend_all(appointments):
    """
    Time Complexity:  O(nlogn)
    Space Complexity: O(n)
    """
    # Sort appointments by start time.
    appointments.sort(key=lambda a: a.start)

    # Iterate through, comparing each consecutive pair of appointments to see if they overlap.
    for i in range(1, len(appointments)):
        if appointments[i - 1].end > appointments[i].start:
            return False

    return True


def test_conflict1():
    appointments = intervals([[1, 4], [2, 5], [7, 9]])
    assert not can_attend_all(appointments)


def test_no_conflicts():
    appointments = intervals([[6, 7], [2, 4], [8, 12]])
    assert can_attend_all(appointments)


def test_conflict2():
    appointments = intervals([[4, 5], [2, 3], [3, 6]])
    assert not can_attend_all(appointments)
