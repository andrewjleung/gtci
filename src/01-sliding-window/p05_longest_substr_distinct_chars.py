from slidingwindow import FixedIntegerSlidingWindow

"""
"""


def longest_substr_distinct(str):
    """
    Time Complexity:  O(n)
    Space Complexity: O(n) or O(1) with a fixed alphabet of characters for the string.
    """
    window_start = 0
    window_char_idxs = {}
    longest_len = 0

    for window_end in range(len(str)):
        char = str[window_end]
        if char in window_char_idxs:
            window_start = max(window_start, window_char_idxs[char] + 1)

        window_char_idxs[char] = window_end
        longest_len = max(longest_len, window_end - window_start + 1)

    return longest_len


def test_ex1():
    i = "aabccbb"
    o = 3

    assert longest_substr_distinct(i) == o


def test_ex2():
    i = "abbbb"
    o = 2

    assert longest_substr_distinct(i) == o


def test_ex3():
    i = "abccde"
    o = 3

    assert longest_substr_distinct(i) == o


def test_ex4():
    i = "abcbdef"
    o = 5

    assert longest_substr_distinct(i) == o
