from src.testutils import contains_same_elements
from collections import deque

"""
Given a string, find all of its permutations preserving the character sequence but changing case.
"""


def string_case_permutations(string):
    """
    Time Complexity:  O(n * 2^n)
    Space Complexity: O(n * 2^n)
    """
    permutations = [string]

    # Iterate through all the characters in the string.
    for i in range(len(string)):
        # Skip digits, we only care about characters.
        if string[i].isalpha():
            # Go through every permutation and swap the case of this letter.
            for j in range(len(permutations)):
                permutation_chars = list(permutations[j])
                permutation_chars[i] = permutation_chars[i].swapcase()
                permutations.append(''.join(permutation_chars))

    return permutations


def test_ex1():
    string = "ad52"
    actual = string_case_permutations(string)
    expected = ["ad52", "Ad52", "aD52", "AD52"]
    assert contains_same_elements(actual, expected)


def test_ex2():
    string = "ab7c"
    actual = string_case_permutations(string)
    expected = ["ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"]
    assert contains_same_elements(actual, expected)
