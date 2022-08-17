from src.datastructures.graph import Graph
from src.testutils import contains_same_elements
from collections import deque

"""
There are `N` tasks, labeled from `0` to `N-1`. Each task can have some 
prerequisite tasks which need to be completed before it can be scheduled. Given 
the number of tasks and a list of prerequisite pairs, write a method to print 
all possible ordering of tasks meeting all prerequisites.
"""


def schedule_tasks(tasks, prerequisites):
    """
    Time Complexity:  O(V! * (V + E))
    Space Complexity: O(V! * (V + E))
    """
    all_orders = []  # O(V!)
    if tasks < 1:
        return all_orders

    sorted_order = []

    # O(V) work to initialize both
    dependent_tasks = {i: [] for i in range(tasks)}  # O(E) space
    task_dependencies = {i: 0 for i in range(tasks)}  # O(V) space

    for prerequisite_pair in prerequisites:  # O(E) iterations
        dependency, dependent = prerequisite_pair[0], prerequisite_pair[1]
        dependent_tasks[dependency].append(dependent)
        task_dependencies[dependent] += 1

    sources = deque()  # O(V) space

    for task, num_dependencies in task_dependencies.items():  # O(V) iterations
        if num_dependencies < 1:
            sources.append(task)

    # O(V) space for recursive call stack
    # O(V!) possible orderings each taking O(V + E) to construct
    get_all_sorts(dependent_tasks, task_dependencies,
                  sources, sorted_order, all_orders)
    return all_orders


def get_all_sorts(graph, in_degrees, sources, sorted_order, all_orders):
    if len(sources) > 0:
        for source in sources:
            sorted_order.append(source)

            # We won't be able to distinguish which sources were created after
            # adding this source to the sorted order since there may be other nodes
            # that already were sources. Instead of backtracking, just use a copy.
            sources_copy = deque(sources)
            sources_copy.remove(source)

            for child in graph[source]:
                in_degrees[child] -= 1
                if in_degrees[child] < 1:
                    sources_copy.append(child)

            get_all_sorts(graph, in_degrees, sources_copy,
                          sorted_order, all_orders)

            sorted_order.remove(source)
            for child in graph[source]:
                in_degrees[child] += 1

    if len(sorted_order) == len(graph):
        all_orders.append(list(sorted_order))


def test_ex1():
    tasks = 3
    prerequisites = [[0, 1], [1, 2]]
    graph = Graph(tasks, prerequisites)
    actual = schedule_tasks(tasks, prerequisites)
    expected = [[0, 1, 2]]
    assert contains_same_elements(actual, expected)


def test_ex2():
    tasks = 4
    prerequisites = [[3, 2], [3, 0], [2, 0], [2, 1]]
    graph = Graph(tasks, prerequisites)
    actual = schedule_tasks(tasks, prerequisites)
    expected = [[3, 2, 0, 1], [3, 2, 1, 0]]
    assert contains_same_elements(actual, expected)


def test_ex3():
    tasks = 6
    prerequisites = [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]
    graph = Graph(tasks, prerequisites)
    actual = schedule_tasks(tasks, prerequisites)
    expected = [
        [0, 1, 4, 3, 2, 5],
        [0, 1, 3, 4, 2, 5],
        [0, 1, 3, 2, 4, 5],
        [0, 1, 3, 2, 5, 4],
        [1, 0, 3, 4, 2, 5],
        [1, 0, 3, 2, 4, 5],
        [1, 0, 3, 2, 5, 4],
        [1, 0, 4, 3, 2, 5],
        [1, 3, 0, 2, 4, 5],
        [1, 3, 0, 2, 5, 4],
        [1, 3, 0, 4, 2, 5],
        [1, 3, 2, 0, 5, 4],
        [1, 3, 2, 0, 4, 5]
    ]
    assert contains_same_elements(actual, expected)
