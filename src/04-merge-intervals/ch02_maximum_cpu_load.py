from interval import (Interval)
import heapq

"""
We are given a list of jobs. Each job has a start time, end time, and CPU load when it is running.
Our goal is to find the maximum CPU load at any time if all the jobs are running on the same 
machine.
"""


class Job(Interval):
    def __init__(self, start, end, load):
        super().__init__(start, end)
        self.load = load

    def __lt__(self, other):
        return super().__lt__(other)


def max_cpu_load(jobs):
    """
    Time Complexity:  O(nlogn)
    Space Complexity: O(n)
    """
    # Sort jobs by starting time.
    jobs.sort(key=lambda j: j.start)

    jobs_heap = []
    current_load = 0
    max_load = 0

    for job in jobs:
        while len(jobs_heap) > 0 and job.start >= jobs_heap[0].end:
            finished_job = heapq.heappop(jobs_heap)
            current_load -= finished_job.load

        heapq.heappush(jobs_heap, job)
        current_load += job.load

        max_load = max(max_load, current_load)

    return max_load


def test_ex1():
    jobs = [Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)]
    assert max_cpu_load(jobs) == 7


def test_ex2():
    jobs = [Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)]
    assert max_cpu_load(jobs) == 15


def test_ex3():
    jobs = [Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)]
    assert max_cpu_load(jobs) == 8
