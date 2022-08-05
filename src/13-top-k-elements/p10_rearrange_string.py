from heapq import (heappush, heappop)


"""
Given a string, find if its letters can be rearranged in such a way that no two
same characters come next to each other.
"""


def rearrange_string(string):
    """
    Time Complexity:  O(n * log n)
    Space Complexity: O(n)
    """
    # Find the frequencies of each character.
    frequencies = {}
    for char in string:  # O(n)
        frequencies[char] = frequencies.get(char, 0) + 1

    # Place all characters with more than one occurrence in a max heap based on
    # their frequencies. Place all distinct characters in the result.
    result = []
    max_heap = []
    for char, freq in frequencies.items():  # O(n * log n)
        if freq < 2:
            result.append(char)
        else:
            heappush(max_heap, (-freq, char))

    # Keep trying to add an a character with the highest frequency to the
    # result. If at any point, only a single character remains with more than
    # one frequency left, return the empty string.
    prev_char = None
    prev_neg_freq = 0
    while len(max_heap) > 0:  # O(n * log n)
        # Place the next character.
        (neg_freq, char) = heappop(max_heap)
        result.append(char)

        # Put the previously placed character back into the heap if it still
        # has more occurrences to place.
        if prev_char is not None and -prev_neg_freq > 0:
            heappush(max_heap, (prev_neg_freq, prev_char))

        # If this is the only character left and it has more than 1 occurrence
        # left to place, we can't complete the string.
        if len(max_heap) < 1 and neg_freq < -1:
            return ''

        # Save this character until after the next placement to avoid putting it
        # next to itself. Remember to decrement its remaining occurrences.
        prev_char = char
        prev_neg_freq = neg_freq + 1

    return ''.join(result)  # O(n)


def verify(original, rearranged):
    if len(original) != len(rearranged):
        return False

    # Check that the two strings are anagrams.
    original_freqs = {}
    rearranged_freqs = {}
    for i in range(len(original)):
        original_freqs[original[i]] = original_freqs.get(original[i], 0) + 1
        rearranged_freqs[rearranged[i]] = rearranged_freqs.get(
            rearranged[i], 0) + 1

    if len(original_freqs) != len(rearranged_freqs):
        return False

    for (char, freq) in original_freqs.items():
        if char not in rearranged_freqs or rearranged_freqs[char] != freq:
            return False

    # Check that no two same characters come next to each other.
    for i in range(1, len(rearranged)):
        if rearranged[i - 1] == rearranged[i]:
            return False

    return True


def test_verify1():
    assert verify("abc", "abc")


def test_verify2():
    assert not verify("ab", "abc")


def test_verify3():
    assert verify("cba", "abc")


def test_verify4():
    assert not verify("cbb", "bbc")


def test_verify5():
    assert not verify("cbaa", "abcb")


def test_verify6():
    assert verify("cbaa", "abca")


def test_ex1():
    string = "aappp"
    actual = rearrange_string(string)
    assert verify(string, actual)


def test_ex2():
    string = "Programming"
    actual = rearrange_string(string)
    assert verify(string, actual)


def test_ex3():
    string = "aapa"
    actual = rearrange_string(string)
    expected = ""
    assert actual == expected
