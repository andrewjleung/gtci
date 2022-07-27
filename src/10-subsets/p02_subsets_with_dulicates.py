"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.
"""


def subsets_w_dupes(elements):
    """
    Time Complexity:  O(nlogn + n * 2^n) = O(n * 2^n)
    Space Complexity: O(n * 2^n)
    """
    results = [[]]
    elements.sort()  # Sort in order to find duplicates.

    # End index is used to keep track of the index from which the last group of subsets was added.
    # This is done so that in the case of a duplicate, we can find where the previous group of
    # subsets started so new subsets can be created only from the previously added group of subsets.
    end_index = 0

    for i in range(len(elements)):
        start_index = 0

        if i > 0 and elements[i] == elements[i - 1]:
            # Use the starting position of the previous group of added subsets in the result array
            # as the starting point of subsets used to generate new subsets.
            start_index = end_index

        # Set the end index to the end of the current results array including all the previously
        # added subsets in preparation for the next iteration of subsets (not including those about
        # to be added).
        end_index = len(results)

        for j in range(start_index, end_index):
            results.append(results[j] + [elements[i]])

    return results


def test_ex1():
    elements = [1, 3, 3]
    assert subsets_w_dupes(elements) == [[], [1], [3], [
        1, 3], [3, 3], [1, 3, 3]]


def test_ex2():
    elements = [1, 5, 3, 3]
    print(subsets_w_dupes(elements))
    assert subsets_w_dupes(elements) == [[], [1], [5], [3], [1, 5], [1, 3], [5, 3], [
        1, 5, 3], [3, 3], [1, 3, 3], [3, 3, 5], [1, 5, 3, 3]]


def test_ex3():
    elements = [3, 3, 3]
    print(subsets_w_dupes(elements))
    assert subsets_w_dupes(elements) == [[], [3], [
        3, 3], [3, 3, 3]]
