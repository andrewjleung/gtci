"""
Given a string and a list of words, find all the starting indices of substrings in the given string
that are a concatenation of all the given words exactly once without any overlapping of words. It is
given that all words are of the same length.
"""


def words_concat(str, words):
    """
    Time Complexity:  O(n * m * len)
    Space Complexity: O(n + m)
    """
    word_freqs = {}
    results = []

    word_len = len(words[0])
    word_count = len(words)

    for word in words:
        if word not in word_freqs:
            word_freqs[word] = 0
        word_freqs[word] += 1

    for window_start in range(len(str) - word_len):
        words_seen = {}

        for word_num in range(word_count):
            word_start_i = window_start + word_num * word_len
            word = str[word_start_i:word_start_i + word_len]

            if word not in word_freqs:
                break

            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            if words_seen[word] > word_freqs[word]:
                break

            if word_num + 1 == word_count:
                results.append(window_start)

    return results


def test_ex1():
    str = "catfoxcat"
    words = ["cat", "fox"]
    o = [0, 3]

    assert words_concat(str, words) == o


def test_ex2():
    str = "catcatfoxfox"
    words = ["cat", "fox"]
    o = [3]

    assert words_concat(str, words) == o


def test_ex3():
    str = "catcatfoxfox"
    words = ["cat", "fox", "cat"]
    o = [0]

    assert words_concat(str, words) == o


def test_ex4():
    str = "acatfoxcat"
    words = ["cat", "fox"]
    o = [1, 4]

    assert words_concat(str, words) == o
