"""
Given a string with lowercase letters only, if you are allowed to replace no more than 'k' letters
with any letter, find the length of the longest substring having the same letters after replacement.
"""


def longest_substr_same_letters_replacement(str, k):
    """
    Time Complexity:  O(N)
    Space Complexity: O(1)
    """
    char_freqs = {}
    max_repeat_letter_count = 0
    max_length = 0
    window_start = 0

    for window_end in range(len(str)):
        right_char = str[window_end]

        # update the frequencies
        if right_char not in char_freqs:
            char_freqs[right_char] = 0
        char_freqs[right_char] += 1

        # update the max repeating letter count
        max_repeat_letter_count = max(
            max_repeat_letter_count, char_freqs[right_char])

        # shrunk the window
        if window_end - window_start + 1 - max_repeat_letter_count > k:
            char_freqs[str[window_start]] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def test_ex1():
    i = "aabccbb"
    k = 2
    o = 5

    assert longest_substr_same_letters_replacement(i, k) == o


def test_ex2():
    i = "abbcb"
    k = 1
    o = 4

    assert longest_substr_same_letters_replacement(i, k) == o


def test_ex3():
    i = "abccde"
    k = 1
    o = 3

    assert longest_substr_same_letters_replacement(i, k) == o


def test_ex4():
    i = "abbacbb"
    k = 2
    o = 6

    assert longest_substr_same_letters_replacement(i, k) == o
