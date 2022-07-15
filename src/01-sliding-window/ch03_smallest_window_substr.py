
"""
Given a string and a pattern, find the smallest substring in the given string which has all the
character occurrences of the given pattern.
"""


def smallest_window_substr(str, pattern):
    """
    Time Complexity:  O(n + m)
    Space Complexity: O(m)
    """
    window_start = 0
    char_freqs = {}
    min_length = None
    min_start = 0
    matches = 0

    for char in pattern:
        if char not in char_freqs:
            char_freqs[char] = 0
        char_freqs[char] += 1

    for window_end in range(len(str)):
        right_char = str[window_end]

        if right_char in char_freqs:
            char_freqs[right_char] -= 1

            if char_freqs[right_char] >= 0:
                matches += 1

        while matches == len(pattern):
            if min_length is None or window_end - window_start + 1 < min_length:
                min_length = window_end - window_start + 1
                min_start = window_start

            left_char = str[window_start]
            if left_char in char_freqs:
                if char_freqs[left_char] == 0:
                    matches -= 1
                char_freqs[left_char] += 1

            window_start += 1

    if min_length is None:
        return ""

    return str[min_start:min_start + min_length]


def test_ex1():
    i = "aabdec"
    p = "abc"
    o = "abdec"

    assert smallest_window_substr(i, p) == o


def test_ex2():
    i = "aabdec"
    p = "abac"
    o = "aabdec"

    assert smallest_window_substr(i, p) == o


def test_ex3():
    i = "abdbca"
    p = "abc"
    o = "bca"

    assert smallest_window_substr(i, p) == o


def test_ex4():
    i = "adcad"
    p = "abc"
    o = ""

    assert smallest_window_substr(i, p) == o
