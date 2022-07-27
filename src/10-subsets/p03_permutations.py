from collections import deque
from src.testutils import contains_same_elements

"""
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of elements of the set. If a set has `n` distinct 
elements, it will have `n!` permutations.
"""


def permutations(nums):
    """
    Time Complexity:  O(n * n!) - creating n! permutations of size n
    Space Complexity: O(n * n!) - the size of a permutation * the number of permutations
    """
    results = []
    # This queue is used to keep track of permutations that aren't of length `n` yet.
    permutations = deque([[]])

    # Iterate through each number, adding it to each position of every permutation.
    for num in nums:
        # Iterate through each permutation.
        for _ in range(len(permutations)):
            permutation = permutations.popleft()

            # Iterate through each position of the permutation for insertion.
            for i in range(len(permutation) + 1):
                new_permutation = list(permutation)
                new_permutation.insert(i, num)

                # If the permutation is ready (of length `n`), accumulate it.
                if len(new_permutation) == len(nums):
                    results.append(new_permutation)
                # Otherwise, put it back on the queue to have the next number added to it.
                else:
                    permutations.append(new_permutation)

    return results


def test_ex1():
    nums = [1, 2, 3, 4, 5]
    actual = permutations(nums)
    expected = [[1, 2, 3], [1, 3, 2], [
        2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert contains_same_elements(actual, expected)


def test_ex2():
    nums = [1, 3, 5]
    actual = permutations(nums)
    expected = [[1, 3, 5], [1, 5, 3], [
        3, 1, 5], [3, 5, 1], [5, 1, 3], [5, 3, 1]]
    assert contains_same_elements(actual, expected)
