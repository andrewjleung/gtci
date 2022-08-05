from heapq import (heappush, heappop)
from collections import deque

"""
You are given a list of tasks that need to be run, in any order, on a server.
Each task will take on CPU interval to execute but once a task has finished, it
has a cooling period during which it can't be run again. If the cooling period
for all tasks is `k` intervals, find the minimum number of CPU intervals that
the server needs to finish all tasks.

If at any time the server can't execute any task then it must stay idle.
"""


def schedule_tasks(tasks, k):
    """
    Time Complexity:  O(n * log n)
    Space Complexity: O(n)
    """
    # Create a mapping from each task to its frequency in the list of tasks.
    frequencies = {}
    for task in tasks:  # O(n)
        frequencies[task] = frequencies.get(task, 0) + 1

    # Add all tasks to a max heap based upon frequency.
    max_heap = []
    for (task, freq) in frequencies.items():  # O (n * log n)
        heappush(max_heap, (-freq, task))

    # Do tasks until the first task has cooled down. This will be at most
    # `k + 1` tasks. If you don't reach that threshold, then you need to sit
    # idle for the remaining time.
    cycle = 0

    while len(max_heap) > 0:
        n = k + 1
        waitlist = []
        while len(max_heap) > 0 and n > 0:
            neg_freq, task = heappop(max_heap)

            if -neg_freq > 1:
                waitlist.append((neg_freq + 1, task))

            cycle += 1
            n -= 1

        # By virtue of always picking the most frequent remaining task, we don't
        # necessarily need to wait for all the tasks just done to be cooled down
        # in order to add them back into the heap, just the first one.
        # This is because the first task done in this batch had to have been the
        # most frequent, and since there should be a consistent picking order,
        # the tasks in this batch should be scheduled in the same exact order in
        # the next batch, give or take any unpicked tasks which are now more
        # frequent than those in this batch.
        for neg_freq, char in waitlist:
            heappush(max_heap, (neg_freq, char))

        # If there are still more tasks to do and we weren't able to do enough
        # tasks in this batch to let the first one cool down, then we need to
        # wait the remaining time idle. No other tasks can be done because they
        # would have already been done if they existed (`n` is not 0, meaning
        # that the max heap ran out first).
        if len(max_heap) > 0:
            cycle += n

    return cycle


def test_ex1():
    tasks = ["a", "a", "b", "b", "c", "c", "d", "d"]
    k = 2
    actual = schedule_tasks(tasks, k)
    expected = 7


def test_ex2():
    tasks = ["a", "b", "a"]
    k = 3
    actual = schedule_tasks(tasks, k)
    expected = 5
