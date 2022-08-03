from heapq import (heappush, heappop)

"""
Given `n` ropes with different lengths, we need to connect these ropes into one
big rope with minimum cost. The cost of connecting two ropes is equal to the sum
of their lengths.
"""


def connect_ropes(ropes):
    """
    Time Complexity:  O(n * log n)
    Space Complexity: O(n)
    """
    min_heap = []
    work = 0

    # Put all ropes in a min heap.
    for rope in ropes:
        heappush(min_heap, rope)

    # While there are at least two ropes left, connect the two smallest ropes,
    # accumulate the work, and add the rope back to the heap.
    while len(min_heap) >= 2:
        new_rope = heappop(min_heap) + heappop(min_heap)
        work += new_rope
        heappush(min_heap, new_rope)

    return work


def test_ex1():
    ropes = [1, 3, 11, 5]
    actual = connect_ropes(ropes)
    expected = 33
    assert actual == expected


def test_ex2():
    ropes = [3, 4, 5, 6]
    actual = connect_ropes(ropes)
    expected = 36
    assert actual == expected


def test_ex3():
    ropes = [1, 3, 11, 5, 2]
    actual = connect_ropes(ropes)
    expected = 42
    assert actual == expected
