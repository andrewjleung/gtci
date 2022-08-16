class E:
    def __init__(self, u, v):
        self.u = u
        self.v = v


class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = []
        for edge in edges:
            self.edges.append(E(edge[0], edge[1]))

    def verify_topological_sort(self, top_sort):
        if len(top_sort) != self.vertices:
            return False

        dependencies = {}
        for edge in self.edges:
            if edge.u not in dependencies:
                dependencies[edge.u] = []
            dependencies[edge.u].append(edge.v)

        seen = set()

        for v in top_sort:
            seen.add(v)

            for u in seen:
                if v in dependencies and u in dependencies[v]:
                    return False

        return True


def test_ts1():
    graph = Graph(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
    assert graph.verify_topological_sort([3, 2, 0, 1])
    assert graph.verify_topological_sort([3, 2, 1, 0])
    assert not graph.verify_topological_sort([3, 0, 2, 1])


def test_ts2():
    graph = Graph(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])
    assert graph.verify_topological_sort([4, 2, 3, 0, 1])
    assert graph.verify_topological_sort([4, 3, 2, 0, 1])
    assert graph.verify_topological_sort([4, 3, 2, 1, 0])
    assert graph.verify_topological_sort([4, 2, 3, 1, 0])
    assert graph.verify_topological_sort([4, 2, 0, 3, 1])
    assert not graph.verify_topological_sort([1, 2, 3, 4, 0])


def test_ts3():
    graph = Graph(7, [[6, 4], [6, 2], [5, 3], [5, 4],
                  [3, 0], [3, 1], [3, 2], [4, 1]])
    assert graph.verify_topological_sort([5, 6, 3, 4, 0, 1, 2])
    assert graph.verify_topological_sort([6, 5, 3, 4, 0, 1, 2])
    assert graph.verify_topological_sort([5, 6, 4, 3, 0, 2, 1])
    assert graph.verify_topological_sort([6, 5, 4, 3, 0, 1, 2])
    assert graph.verify_topological_sort([5, 6, 3, 4, 0, 2, 1])
    assert graph.verify_topological_sort([5, 6, 3, 4, 1, 2, 0])
    assert not graph.verify_topological_sort([1, 2, 0, 4, 3, 6, 5])
