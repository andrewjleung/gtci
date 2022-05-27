"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string.
"""


def permutation_in_string(str, pattern):
    """
    Time Complexity:  O(n + m)
    Space Complexity: O(m)
    """
    window_start = 0
    char_freqs = {}
    matches = 0

    for char in pattern:
        if char not in char_freqs:
            char_freqs[char] = 0
        char_freqs[char] += 1

    for window_end in range(len(str)):
        right_char = str[window_end]

        if right_char in char_freqs:
            char_freqs[right_char] -= 1

            if char_freqs[right_char] == 0:
                matches += 1

        if matches == len(char_freqs):
            return True

        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_freqs:
                if char_freqs[left_char] == 0:
                    matches -= 1
                char_freqs[left_char] += 1

    return False


def test_ex1():
    i = "oidbcaf"
    p = "abc"
    o = True

    assert permutation_in_string(i, p) == o


def test_ex2():
    i = "odicf"
    p = "dc"
    o = False

    assert permutation_in_string(i, p) == o


def test_ex3():
    i = "bcdxabcdy"
    p = "bcdyabcdx"
    o = True

    assert permutation_in_string(i, p) == o


def test_ex4():
    i = "aaacb"
    p = "abc"
    o = True

    assert permutation_in_string(i, p) == o
