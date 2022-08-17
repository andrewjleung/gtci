from collections import deque

"""
There is a dictionary containing words from an alien language for which we don't
know the ordering of letters. Write a method to find the correct ordering of
letters in the alien language. It is given that the input is a valid dictionary
and there exists an ordering among its letters.
"""


def find_alien_ordering(dictionary):
    """
    `V` is the number of letters, `N` is the number of words. The number of 
    "edges" is bound by the number of words because each pair of adjacent words 
    can give at most a single rule in the language.
    Time Complexity:  O(V + N)
    Space Complexity: O(V + N)
    """
    if len(dictionary) < 1:
        return ""

    adjacency_list = {}
    in_degrees = {}

    # Initialize the adjacency list and in-degrees for all characters.
    for word in dictionary:
        for char in word:
            adjacency_list[char] = []
            in_degrees[char] = 0

    # For every two adjacent words in the dictionary, create dependencies based
    # on their first different characters.
    for i in range(len(dictionary) - 1):
        word1, word2 = dictionary[i], dictionary[i + 1]
        for j in range(min(len(word1), len(word2))):
            char1, char2 = word1[j], word2[j]
            if char1 != char2:
                adjacency_list[char1].append(char2)
                in_degrees[char2] += 1
                break

    sources = deque()

    for letter, in_degree in in_degrees.items():
        if in_degree < 1:
            sources.append(letter)

    letter_ordering = []

    while len(sources) > 0:
        source = sources.popleft()
        letter_ordering.append(source)

        for child in adjacency_list[source]:
            in_degrees[child] -= 1
            if in_degrees[child] < 1:
                sources.append(child)

    # Don't need to worry about detecting cycles since we are guaranteed that
    # the dictionary is well-formed and contains an ordering.
    return ''.join(letter_ordering)


def test_ex1():
    dictionary = ["ba", "bc", "ac", "cab"]
    actual = find_alien_ordering(dictionary)
    expected = "bac"
    assert actual == expected


def test_ex2():
    dictionary = ["cab", "aaa", "aab"]
    actual = find_alien_ordering(dictionary)
    expected = "cab"
    assert actual == expected


def test_ex3():
    dictionary = ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
    actual = find_alien_ordering(dictionary)
    expected = "ywxz"
    assert actual == expected
