"""
Every non-negative integer N has a binary representation, for example, 8 can be 
represented as "1000" in binary and 7 as "0111" in binary.

The complement of a binary representation is the number in binary that we get 
when we change every 1 to a 0 and every 0 to a 1. For example, the binary 
complement of "1010" is "0101".

For a given positive number N in base-10, return the complement of its binary 
representation as a base-10 integer.
"""


def base10_complement(num):
    """
    Time Complexity:  O(b) - `b` is the number of bits required to store the number 
    Space Complexity: O(1)
    """
    bit_count = 0
    n = num

    # Keep bitshifting right (dividing by two) until the number is 0.
    # This effectively will count the number of bits needed to represent the
    # number.
    while n > 0:
        bit_count += 1
        n = n >> 1

    # `2^bit_count` will equal the power of two with a one in the
    # `bit_count + 1` digit. This number - 1 will equal the number with
    # `bit_count` 1's.
    all_bits_set = pow(2, bit_count) - 1

    # The complement of a number is the number XOR the number with all of its
    # significant bits set to 1s.
    return num ^ all_bits_set


def test_ex1():
    num = 8
    actual = base10_complement(num)
    expected = 7
    assert actual == expected


def test_ex2():
    num = 10
    actual = base10_complement(num)
    expected = 5
    assert actual == expected


def test_ex3():
    num = 7
    actual = base10_complement(num)
    expected = 0
    assert actual == expected


def test_ex4():
    num = 6
    actual = base10_complement(num)
    expected = 1
    assert actual == expected
