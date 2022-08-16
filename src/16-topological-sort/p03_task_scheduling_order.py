from src.datastructures.graph import Graph
from collections import deque

"""
There are `n` tasks, labeled from `0` to `n - 1`. Each task can have some 
prerequisite tasks which need to be completed before it can be scheduled. Given
the number of tasks and a list of prerequisite pairs, write a method to find the
ordering of tasks we should pick to finish all tasks.
"""


def schedule_tasks(tasks, prerequisites):
    """
    Time Complexity:  O(n + p)
    Space Complexity: O(n + p)
    """
    results = []
    if tasks <= 0:
        return results

    dependent_tasks = {i: [] for i in range(tasks)}
    task_dependencies = {i: 0 for i in range(tasks)}

    for prerequisite_pair in prerequisites:
        prereq = prerequisite_pair[0]
        dependent = prerequisite_pair[1]
        dependent_tasks[prereq].append(dependent)
        task_dependencies[dependent] += 1

    schedulable_tasks = deque()

    for task, num_dependencies in task_dependencies.items():
        if num_dependencies < 1:
            schedulable_tasks.append(task)

    while len(schedulable_tasks) > 0:
        schedulable_task = schedulable_tasks.popleft()
        results.append(schedulable_task)
        for dependent_task in dependent_tasks[schedulable_task]:
            task_dependencies[dependent_task] -= 1
            if task_dependencies[dependent_task] < 1:
                schedulable_tasks.append(dependent_task)

    if len(results) != tasks:
        return []

    return results


def test_ex1():
    tasks = 3
    prerequisites = [[0, 1], [1, 2]]
    graph = Graph(tasks, prerequisites)
    actual = schedule_tasks(tasks, prerequisites)
    assert graph.verify_topological_sort(actual)


def test_ex2():
    tasks = 3
    prerequisites = [[0, 1], [1, 2], [2, 0]]
    graph = Graph(tasks, prerequisites)
    actual = schedule_tasks(tasks, prerequisites)
    assert not graph.verify_topological_sort(actual)


def test_ex3():
    tasks = 6
    prerequisites = [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]
    graph = Graph(tasks, prerequisites)
    actual = schedule_tasks(tasks, prerequisites)
    assert graph.verify_topological_sort(actual)
