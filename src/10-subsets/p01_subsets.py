"""
Given a set with distinct elements, find all of its distinct subsets.
"""


def subsets(elements):
    """
    Time Complexity:  O(n * 2^n) - the number of subsets doubles for each element, each subset is O(n) in size
    Space Complexity: O(n * 2^n)
    """
    results = [[]]

    # O(2^n) subsets will be created.
    for element in elements:
        for i in range(len(results)):
            # Creating the new subset takes O(n).
            results.append(results[i] + [element])

    return results


def test_ex1():
    elements = [1, 3]
    assert subsets(elements) == [[], [1], [3], [1, 3]]


def test_ex2():
    elements = [1, 5, 3]
    foo = subsets(elements)
    print(foo)
    assert subsets(elements) == [[], [1], [5], [1, 5], [
        3], [1, 3], [5, 3], [1, 5, 3]]
