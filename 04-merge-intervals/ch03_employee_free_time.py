from interval import (Interval, intervals, intervals_eq)
import heapq

"""
For `K` employees, we are given a list of intervals representing each employee's working hours. Our
goal is to determine if there is a free interval which is common to all employees. You can assume
that each list of employee working hours is sorted on the start time.
"""


def find_employee_free_time_all_intervals(schedules):
    """
    Time Complexity:  O(nlogn)
    Space Complexity: O(n)
    """

    # Merge schedules.
    all_work_time = [i for schedule in schedules for i in schedule]
    all_work_time.sort(key=lambda schedule: schedule.start)

    free_time = []

    # Find free time.
    for i in range(1, len(all_work_time)):
        if all_work_time[i - 1].end < all_work_time[i].start:
            free_time.append(
                Interval(all_work_time[i - 1].end, all_work_time[i].start))

    return free_time


class EmployeeInterval():
    def __init__(self, interval, employee_index, interval_index):
        self.interval = interval
        self.employee_index = employee_index
        self.interval_index = interval_index

    def __lt__(self, other):
        return self.interval.start < other.interval.start


def find_employee_free_time(schedules):
    """
    Time Complexity:  O(nlogk) - k is the number of employees
    Space Complexity: O(k)
    """
    work_heap = []
    free_time = []

    for i in range(len(schedules)):
        heapq.heappush(work_heap, EmployeeInterval(schedules[i][0], i, 0))

    previous_interval = work_heap[0].interval

    while len(work_heap) > 0:
        top = heapq.heappop(work_heap)

        if previous_interval.end < top.interval.start:
            free_time.append(
                Interval(previous_interval.end, top.interval.start))
            previous_interval = top.interval
        else:
            if previous_interval.end < top.interval.end:
                previous_interval = top.interval

        employee_schedule = schedules[top.employee_index]
        if len(employee_schedule) > top.interval_index + 1:
            heapq.heappush(work_heap, EmployeeInterval(
                employee_schedule[top.interval_index + 1], top.employee_index, top.interval_index + 1))

    return free_time


def test_ex1():
    schedules = [intervals([[1, 3], [5, 6]]), intervals([[2, 3], [6, 8]])]
    actual = intervals([[3, 5]])
    expected = find_employee_free_time(schedules)
    assert intervals_eq(actual, expected)


def test_ex2():
    schedules = [intervals([[1, 3], [9, 12]]), intervals([[2, 4], [6, 8]])]
    actual = intervals([[4, 6], [8, 9]])
    expected = find_employee_free_time(schedules)
    assert intervals_eq(actual, expected)


def test_ex3():
    schedules = [intervals([[1, 3], [2, 4]]), intervals([[3, 5], [7, 9]])]
    actual = intervals([[5, 7]])
    expected = find_employee_free_time(schedules)
    assert intervals_eq(actual, expected)
