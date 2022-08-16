from src.datastructures.graph import (Graph)
from collections import deque

"""
Topological sort of a directed graph (a graph with unidirectional edges) is a 
linear ordering of its vertices such that for every directed edge (U, V) from 
vertex `U` to vertex `V`, `U` comes before `V` in the ordering.

Given a directed graph, find the topological ordering of its vertices.
"""


def topological_sort(graph):
    """
    Time Complexity:  O(V + E)
    Space Complexity: O(V + E)
    """
    result = []  # O(V)
    if graph.vertices < 1:
        return result

    # Initialize the adjacency list and inbound edges mapping.
    adjacency_list = {i: [] for i in range(graph.vertices)}  # O(E)
    node_inbound_edges = {i: 0 for i in range(graph.vertices)}  # O(V)

    # Populate the adjacency list and inbound edges mapping based upon the edges.
    for edge in graph.edges:  # O(E)
        adjacency_list[edge.u].append(edge.v)
        node_inbound_edges[edge.v] += 1

    sources = deque()  # O(V)

    # Add all sources to the queue. Sources have no inbound edges.
    for node, inbound_edges in node_inbound_edges.items():  # O(V)
        if inbound_edges == 0:
            sources.append(node)

    while len(sources) > 0:  # O(V)
        # Pop off a source and add it to the ordering. It is safe to add at this
        # point because nothing that it depends on hasn't already been added to
        # the ordering.
        source = sources.popleft()
        result.append(source)

        # Since this source has been added to the ordering, any vertices that
        # depend on this source no longer need to consider that respective
        # inbound edge. Decrement it from their inbound edges.
        for child in adjacency_list[source]:
            node_inbound_edges[child] -= 1

            # If at this point this dependent vertex has no more inbound edges,
            # this means that every node it depends on has been placed. It can
            # be safely placed at any point from now on. Queue it.
            if node_inbound_edges[child] == 0:
                sources.append(child)

    # If not all the vertices were sorted, this indicates a cycle was present.
    if len(result) != graph.vertices:
        return None

    return result


def test_ex1():
    graph = Graph(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
    assert graph.verify_topological_sort(topological_sort(graph))


def test_ex2():
    graph = Graph(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])
    assert graph.verify_topological_sort(topological_sort(graph))


def test_ex3():
    graph = Graph(7, [[6, 4], [6, 2], [5, 3], [5, 4],
                  [3, 0], [3, 1], [3, 2], [4, 1]])
    assert graph.verify_topological_sort(topological_sort(graph))
