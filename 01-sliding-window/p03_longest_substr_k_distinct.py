#!/usr/bin/env python3
import math

"""
Given a string, find the length of the longest substring in it with no more than K distinct
characters.
"""


def add_occurrence(dct, key):
    if key not in dct:
        dct[key] = 0

    dct[key] += 1


def sub_occurrence(dct, key):
    dct[key] -= 1

    if dct[key] == 0:
        del dct[key]


def longest_substr_k_distinct(str, k):
    """
    Time Complexity:  O(N)
    Space Complexity: O(K)
    """
    # Initialize accumulators
    char_occurs = {}
    longest_length = -math.inf
    window_start = 0

    for window_end in range(len(str)):
        add_occurrence(char_occurs, str[window_end])

        while len(char_occurs) > k:
            sub_occurrence(char_occurs, str[window_start])
            window_start += 1

        longest_length = max(longest_length, window_end - window_start + 1)

    return longest_length


def test_ex1():
    i = "araaci"
    k = 2
    o = 4  # "araa"

    assert longest_substr_k_distinct(i, k) == o


def test_ex2():
    i = "araaci"
    k = 1
    o = 2  # "aa"

    assert longest_substr_k_distinct(i, k) == o


def test_ex3():
    i = "cbbebi"
    k = 3
    o = 5  # "bbebi"

    assert longest_substr_k_distinct(i, k) == o
