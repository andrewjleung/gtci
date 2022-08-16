from src.datastructures.graph import Graph
from collections import deque

"""
There are `n` tasks, labeled from `0` to `n - 1`. Each task can have some 
prerequisite tasks which need to be completed before it can be scheduled. Given
the number of tasks and a list of prerequisite pairs, find out if it is possible
to schedule all tasks.
"""


def can_be_scheduled(tasks, prerequisites):
    """
    Time Complexity:  O(n + p)
    Space Complexity: O(n + p)
    """
    if tasks <= 0:
        return False

    # Create a graph.
    graph = Graph(tasks, prerequisites)
    dependent_tasks = {i: [] for i in range(graph.vertices)}  # O(p)
    task_dependencies = {i: 0 for i in range(graph.vertices)}  # O(n)

    # Populate the adjacency list and inbound edges based upon the prereqs.
    for prereq_pair in graph.edges:   # O(p)
        dependent_tasks[prereq_pair.u].append(prereq_pair.v)
        task_dependencies[prereq_pair.v] += 1

    schedulable_tasks = deque()   # O(n)
    tasks_scheduled = 0

    # Add all immediately schedulable (no dependencies) tasks to the task queue.
    for task, dependencies in task_dependencies.items():   # O(n)
        if dependencies < 1:
            schedulable_tasks.append(task)

    # Try to schedule all tasks using topological sort.
    while len(schedulable_tasks) > 0:  # O(n)
        schedulable_task = schedulable_tasks.popleft()
        tasks_scheduled += 1
        for dependent_task in dependent_tasks[schedulable_task]:
            task_dependencies[dependent_task] -= 1
            if task_dependencies[dependent_task] < 1:
                schedulable_tasks.append(dependent_task)

    # If we couldn't schedule all tasks, then there was a cyclic prereq.
    return tasks_scheduled == tasks


def test_ex1():
    tasks = 3
    prerequisites = [[0, 1], [1, 2]]
    actual = can_be_scheduled(tasks, prerequisites)
    expected = True
    assert actual == expected


def test_ex2():
    tasks = 3
    prerequisites = [[0, 1], [1, 2], [2, 0]]
    actual = can_be_scheduled(tasks, prerequisites)
    expected = False
    assert actual == expected


def test_ex3():
    tasks = 6
    prerequisites = [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]
    actual = can_be_scheduled(tasks, prerequisites)
    expected = True
    assert actual == expected
