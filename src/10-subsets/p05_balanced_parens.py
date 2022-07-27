from src.testutils import contains_same_elements
from collections import deque

"""
For a given number `N`, write a function to generate all combinations of `N` pairs of balanced
parentheses.
"""


class ParenthesesString:
    def __init__(self, string, opens, closes):
        self.string = string
        self.opens = opens
        self.closes = closes


def balanced_parens(n):
    """
    Time Complexity:  O(n * 2^n) - this is not exactly accurate, but ignores restrictions on correct parens.
    Space Complexity: O(n * 2^n) - same as above.
    """
    results = []
    ps_queue = deque([ParenthesesString("", 0, 0)])

    while len(ps_queue) > 0:
        ps = ps_queue.popleft()

        # If we can possibly add another open paren without going over `n`, do so.
        if ps.opens < n:
            string = ps.string + "("
            opens = ps.opens + 1
            closes = ps.closes
            new_ps = ParenthesesString(string, opens, closes)
            ps_queue.append(new_ps)

        # If we can possibly add a close paren if there are unclosed open parens, do so.
        if ps.opens > ps.closes:
            string = ps.string + ")"
            opens = ps.opens
            closes = ps.closes + 1

            # If adding this close paren reaches `n`, don't add it to the queue.
            # Instead, accumulate the string.
            if opens == closes and closes == n:
                results.append(string)
                continue

            new_ps = ParenthesesString(string, opens, closes)
            ps_queue.append(new_ps)

    return results


def test_ex1():
    n = 2
    actual = balanced_parens(n)
    expected = ["(())", "()()"]
    assert contains_same_elements(actual, expected)


def test_ex2():
    n = 3
    actual = balanced_parens(n)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert contains_same_elements(actual, expected)
