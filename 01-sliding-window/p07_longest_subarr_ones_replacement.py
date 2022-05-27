"""
Given an array containing 0s and 1s, if you are allowed to replace no more than 'k' 0s with 1s, find
the length of the longest contiguous subarray having all 1s.
"""

# TODO: the actual solution proposes keeping track of a max_ones_count rather than the number of
# zeros, and while that does end up with a runtime of O(n) instead of O(n + n) as this one is, they
# are both asymptotically the same. Not sure if they are both correct in the same way however.


def longest_subarr_ones_replacement(arr, k):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    max_len = 0
    num_zeros = 0
    window_start = 0

    for window_end in range(len(arr)):

        if arr[window_end] == 0:
            num_zeros += 1

        while num_zeros > k:
            if arr[window_start] == 0:
                num_zeros -= 1
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)

    return max_len


def test_ex1():
    i = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    k = 2
    o = 6

    assert longest_subarr_ones_replacement(i, k) == o


def test_ex2():
    i = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    k = 3
    o = 9

    assert longest_subarr_ones_replacement(i, k) == o
