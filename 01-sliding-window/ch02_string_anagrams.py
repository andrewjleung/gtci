
""" 
Given a string and a pattern, find all anagrams of the pattern in the given string by listing the 
starting indices of each anagram.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters
while finding permutations of a string, we get N! permutations (or anagrams) of a string having N
characters.
"""


def string_anagrams(str, pattern):
    """
    Time Complexity:  O(n + m)
    Space Complexity: O(n + m)
    """
    window_start = 0
    char_freqs = {}
    matches = 0
    results = []

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
            results.append(window_start)

        if window_end >= len(pattern) - 1:
            left_char = str[window_start]

            if left_char in char_freqs:
                if char_freqs[left_char] == 0:
                    matches -= 1
                char_freqs[left_char] += 1

            window_start += 1

    return results


def test_ex1():
    i = "ppqp"
    p = "pq"
    o = [1, 2]

    assert string_anagrams(i, p) == o


def test_ex1():
    i = "abbcabc"
    p = "abc"
    o = [2, 3, 4]

    assert string_anagrams(i, p) == o
