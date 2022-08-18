from heapq import (heappush, heappop)
from collections import deque
import math

"""
Given a string and a number `k`, find if the string can be rearranged such that
the same characters are at least `k` distance apart from each other.
"""


def rearrange_string_k_distance_apart(string, k):
    """
    Time Complexity:  O(n * log n)
    Space Complexity: O(n)
    """
    if k <= 1:
        return string

    # Get the frequencies of every character.
    frequencies = {}
    for char in string:  # O(n)
        frequencies[char] = frequencies.get(char, 0) + 1

    # Add all characters to a max heap based upon frequency.
    max_heap = []  # Characters that can be placed.
    for char, freq in frequencies.items():  # O(n * log n)
        heappush(max_heap, (-freq, char))

    # While the max heap is not empty:
    #   Add the character with the most remaining occurrences to the result, and
    #   then add that character to a min heap based upon the index where it was
    #   just placed. This will be used to keep track of characters that can't
    #   yet be placed.

    #   Add all previously placed characters which can now be placed again back
    #   to the max heap.

    result = []
    cant_place = deque()  # Characters that can't yet be placed.
    while len(max_heap) > 0:  # O(n * log n)
        neg_freq, char = heappop(max_heap)
        result.append(char)
        cant_place.append((char, neg_freq + 1))

        # In order for the length of `cant_place` to be comparable to `k`, we
        # need to place ALL characters that we've just placed into it,
        # regardless of if they actually can be placed again. Otherwise, we need
        # to keep track of the exact index each element was placed.
        if len(cant_place) == k:
            char, neg_freq = cant_place.popleft()

            # If the character can't be placed again, don't put it back in the
            # heap.
            if -neg_freq > 0:
                heappush(max_heap, (neg_freq, char))

    # We are always pushing regardless of frequency to the cant_place queue.
    # We can't trust that it being non-empty implies that we couldn't place all
    # characters. I don't love this, but it's necessary.
    if len(result) != len(string):
        return ''

    return ''.join(result)


def verify(original, rearr, k):
    sorted_original = sorted(original)
    sorted_rearr = sorted(rearr)

    if sorted_original != sorted_rearr:
        return False

    last_seen = {}
    for i in range(len(rearr)):
        char = rearr[i]

        if i < last_seen.get(char, -math.inf) + k:
            return False

        last_seen[char] = i

    return True


def test_verify1():
    assert verify("mmpp", "mpmp", 2)


def test_verify2():
    assert verify("mmpp", "pmpm", 2)


def test_verify3():
    assert not verify("mmpp", "mpmp", 3)


def test_ex1():
    string = "mmpp"
    k = 2
    actual = rearrange_string_k_distance_apart(string, k)
    assert verify(string, actual, k)


def test_ex2():
    string = "Programming"
    k = 3
    actual = rearrange_string_k_distance_apart(string, k)
    assert verify(string, actual, k)


def test_ex3():
    string = "aab"
    k = 2
    actual = rearrange_string_k_distance_apart(string, k)
    assert verify(string, actual, k)


def test_ex4():
    string = "aappa"
    k = 3
    actual = rearrange_string_k_distance_apart(string, k)
    expected = ""
    assert actual == expected
