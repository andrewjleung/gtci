from heapq import (heappush, heappop)

"""
Given a string, sort it based on the decreasing frequency of its characters.
"""


def frequency_sort(string):
    """
    Time Complexity:  O(n * log n)
    Space Complexity: O(n)
    """
    # Create a mapping of characters to their frequencies.
    frequencies = {}
    for char in string:  # O(n)
        frequencies[char] = frequencies.get(char, 0) + 1

    # Sort the character-frequency pairs using a max heap.
    max_heap = []
    for (char, freq) in frequencies.items():
        heappush(max_heap, (-freq, char))

    # Create the new string.
    result = []
    while len(max_heap) > 0:  # O(d) iterations, O(n) work overall
        freq, char = heappop(max_heap)
        for _ in range(-freq):
            result.append(char)

    return ''.join(result)


def test_ex1():
    string = "Programming"
    actual = frequency_sort(string)
    expected = "ggmmrrPaino"
    assert actual == expected


def test_ex2():
    string = "abcbab"
    actual = frequency_sort(string)
    expected = "bbbaac"
    assert actual == expected
