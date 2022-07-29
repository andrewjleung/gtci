"""
Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given
array greater than a given `key`.

Assume the given array is a circular list, which means that the last letter is assumed to be 
connected with the first letter. This also means that the smallest letter in the given array is
greater than the last letter of the array and is also the first letter in the array.

Write a function to return the next letter of the given `key`.
"""


def next_letter(letters, key):
    """
    Time Complexity:  O(logn)
    Space Complexity: O(1)
    """
    if len(letters) < 1:
        raise ValueError("Letters array cannot be empty.")

    start = 0
    end = len(letters) - 1

    while start <= end:
        middle = start + (end - start) // 2

        if key < letters[middle]:
            end = middle - 1
        else:
            # This also includes the case if the key is the middle. We defer to searching the upper
            # half because this will contain solely elements greater than the key, eventually giving
            # us the first element of that range which is the answer.
            start = middle + 1

    # This modulus is all you need to create circularity.
    # If the key is greater than or equal to the last letter, then `start`` will increment in that
    # last iteration to equal the length of the letters array, circling back to the first element.
    return letters[start % len(letters)]


def test_ex1():
    letters = ['a', 'c', 'f', 'h']
    key = 'f'
    actual = next_letter(letters, key)
    expected = 'h'
    assert actual == expected


def test_ex2():
    letters = ['a', 'c', 'f', 'h']
    key = 'b'
    actual = next_letter(letters, key)
    expected = 'c'
    assert actual == expected


def test_ex3():
    letters = ['a', 'c', 'f', 'h']
    key = 'm'
    actual = next_letter(letters, key)
    expected = 'a'
    assert actual == expected


def test_ex4():
    letters = ['a', 'c', 'f', 'h']
    key = 'h'
    actual = next_letter(letters, key)
    expected = 'a'
    assert actual == expected


def test_ex4():
    letters = ['a']
    key = 'a'
    actual = next_letter(letters, key)
    expected = 'a'
    assert actual == expected


def test_ex5():
    letters = ['b', 'c', 'd']
    key = 'a'
    actual = next_letter(letters, key)
    expected = 'b'
    assert actual == expected
