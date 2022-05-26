from p03_longest_substr_k_distinct import longest_substr_k_distinct

"""
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be
given two baskets, and your goal is to pick as many fruits as possible to be placed in the given 
baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has
the following restrictions:

1. Each basket can have only one type of fruit. There is no limit to how many fruit a basket can
hold.
2. You can start with any tree, but you can't skip a tree once you have started.
3. You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you
have to pick from a third fruit type.

Write a function to return the max number of fruits in both baskets.
"""


def fruits_into_baskets(str):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    return longest_substr_k_distinct(str, 2)


def test_ex1():
    i = "ABCAC"
    o = 3

    assert fruits_into_baskets(i) == o


def test_ex2():
    i = "ABCBBC"
    o = 5

    assert fruits_into_baskets(i) == o
