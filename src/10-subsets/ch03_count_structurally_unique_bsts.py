"""
Given a number `n`, write a function to return the count of structurally unique Binary Search Trees
(BST) that can store values 1 to `n`.
"""

"""
Time Complexity:  O(n^2)
    - With memoization, each subproblem for each subset of the range 1-n is only calculated once.
    - A range/array/whatever has O(n^2) subsets.

Space Complexity: O(n)
    - The memo will only hold at most `n` elements, one for each possible subproblem.
"""


class CountStructurallyUniqueBSTs:
    def __init__(self):
        self.memo = {}

    def count_unique_bsts(self, n):
        if n in self.memo:
            return self.memo[n]

        if n <= 1:
            return 1

        count = 0

        for i in range(1, n + 1):
            left_count = self.count_unique_bsts(i - 1)
            right_count = self.count_unique_bsts(n - i)
            count += left_count * right_count

        self.memo[n] = count

        return count


def test_ex1():
    n = 2
    csubst = CountStructurallyUniqueBSTs()
    actual = csubst.count_unique_bsts(n)
    expected = 2
    assert actual == expected


def test_ex2():
    n = 3
    csubst = CountStructurallyUniqueBSTs()
    actual = csubst.count_unique_bsts(n)
    expected = 5
    assert actual == expected
