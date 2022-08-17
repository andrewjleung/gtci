from collections import deque

"""
Given a sequence `original_seq` and an array of sequences, write a method to 
find if `original_seq` can be uniquely reconstructed from the array of 
sequences.

Unique reconstruction means that we need to find if `original_seq` is the only
sequence such that all sequences in the array are subsequences of it.
"""


def can_reconstruct_sequence(original_seq, seqs):
    """
    `V` is the number of distinct numbers within the sequences.
    `N` is the total number of elements in all sequences. The number of edges is
    bound by this number since an edge is made for every pair of numbers in the
    sequences.
    Time Complexity:  O(V + N)
    Space Complexity: O(V + N)
    """
    if len(original_seq) < 1:
        return False

    # Initialize the adjacency list and in-degrees map for every element in the
    # list of sequences. It is not guaranteed that all numbers in the original
    # sequence will appear in the given sequences and vice versa.
    adjacency_list = {}  # O(N) space
    in_degrees = {}  # O(V) space

    for seq in seqs:  # O(N) iterations
        for num in seq:
            adjacency_list[num] = []
            in_degrees[num] = 0

    # If there aren't rules for every number in the original sequence, then
    # there will be ambiguity and thus we won't be able to construct a sequence.
    if len(in_degrees) != len(original_seq):
        return False

    # Convert sequences into edges. For every adjacent pair of numbers in a
    # sequence, a single edge is formed where the latter number depends on the
    # former number.
    for seq in seqs:  # O(N) iterations
        if len(seq) > 1:
            for i in range(len(seq) - 1):
                num1, num2 = seq[i], seq[i + 1]
                adjacency_list[num1].append(num2)
                in_degrees[num2] += 1

    sources = deque()

    for el, in_degree in in_degrees.items():  # O(N) iterations
        if in_degree < 1:
            sources.append(el)

    # This is not necessary since we only need the length of the reconstruction.
    reconstructed = []  # O(V) space

    # Do a topological sort. If at any point, there is more than a single source
    # node that can be placed in the ordering, then a unique ordering is not
    # possible.
    while len(sources) > 0:  # O(N) work to remove all edges.
        if len(sources) > 1:
            return False

        # If the reconstruction goes past the length of the original sequence,
        # then there were extra numbers in the sequences.
        if len(reconstructed) >= len(original_seq):
            return False

        # If the next element added to the reconstruction is different than the
        # corresponding element in the original ordering, then an unambiguous
        # reconstruction is not possible. This may happen if the ordering is
        # incorrect or contains different numbers.
        if original_seq[len(reconstructed)] != sources[0]:
            return False

        source = sources.popleft()
        reconstructed.append(source)

        for child in adjacency_list[source]:
            in_degrees[child] -= 1
            if in_degrees[child] < 1:
                sources.append(child)

    # If a cycle is present, then there is no way to reconstruct either.
    return len(reconstructed) == len(original_seq)


def test_ex1():
    original_seq = [1, 2, 3, 4]
    seqs = [[1, 2], [2, 3], [3, 4]]
    actual = can_reconstruct_sequence(original_seq, seqs)
    expected = True
    assert actual == expected


def test_ex2():
    original_seq = [1, 2, 3, 4]
    seqs = [[1, 2], [2, 3], [2, 4]]
    actual = can_reconstruct_sequence(original_seq, seqs)
    expected = False
    assert actual == expected


def test_ex3():
    original_seq = [3, 1, 4, 2, 5]
    seqs = [[3, 1, 5], [1, 4, 2, 5]]
    actual = can_reconstruct_sequence(original_seq, seqs)
    expected = True
    assert actual == expected
