from collections import deque

"""
We are given an undirected graph that has characteristics of a k-ary tree. In
such a graph, we can choose any node as the root to make a k-ary tree. The root
(or the tree) with the minimum height will be called Minimum Height Tree (MHT).
There can be multiple MHTs for a graph. In this problem, we need to find all 
those roots which give us MHTs. Write a method to find all MHTs of the given
graph and return a list of their roots.
"""


def min_height_trees(vertices, edges):
    """
    Time Complexity:  O(V + E)
    Space Complexity: O(V + E)
    """
    if vertices < 1:
        return []

    if vertices < 2:
        return [0]

    adjacency_list = {i: [] for i in range(vertices)}
    in_degrees = {i: 0 for i in range(vertices)}

    for edge in edges:
        u, v = edge[0], edge[1]
        # The graph is undirected.
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
        in_degrees[u] += 1
        in_degrees[v] += 1

    leaves = deque()

    for node, in_degree in in_degrees.items():
        if in_degree < 2:
            leaves.append(node)

    total_nodes = vertices
    # We want to stop removing leaves as soon as there are only at most two
    # nodes left. If there are two remaining, we know that their MHTs must be
    # the same height because we've removed the same amount of depth from each
    # of them.
    while total_nodes > 2:
        # We don't want to remove a leaf at a time, we want to remove all leaves
        # at once. This is because we are trying to remove a single depth from
        # every non-leaf root. Otherwise we risk removing a MHT root.
        num_leaves = len(leaves)
        total_nodes -= num_leaves
        for _ in range(num_leaves):
            leaf = leaves.popleft()
            for child in adjacency_list[leaf]:
                in_degrees[child] -= 1
                # This check needs to be exactly equal to 1 to avoid duplicate
                # nodes being added to the leaves, say in the case that multiple
                # leaves are being removed from the same child.
                if in_degrees[child] == 1:
                    leaves.append(child)

    return list(leaves)


def test_ex1():
    vertices = 5
    edges = [[0, 1], [1, 2], [1, 3], [2, 4]]
    actual = min_height_trees(vertices, edges)
    expected = [1, 2]
    assert actual == expected


def test_ex2():
    vertices = 4
    edges = [[0, 1], [0, 2], [2, 3]]
    actual = min_height_trees(vertices, edges)
    expected = [0, 2]
    assert actual == expected


def test_ex3():
    vertices = 4
    edges = [[0, 1], [1, 2], [1, 3]]
    actual = min_height_trees(vertices, edges)
    expected = [1]
    assert actual == expected
