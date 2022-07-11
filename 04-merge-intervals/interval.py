class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

    def __eq__(self, other):
        return isinstance(other, Interval) and self.start == other.start and self.end == other.end


def intervals(arr):
    return [Interval(start, end) for [start, end] in arr]


def test_intervals_empty():
    assert intervals([]) == []


def test_intervals_non_empty():
    actual = intervals([[1, 2], [3, 4], [4, 5]])
    expected = [Interval(1, 2), Interval(3, 4), Interval(4, 5)]

    for i in range(len(actual)):
        assert actual[i].start == expected[i].start and actual[i].end == expected[i].end


def intervals_eq(a, b):
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if a[i].start != b[i].start or a[i].end != b[i].end:
            return False

    return True
