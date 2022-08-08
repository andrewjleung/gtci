from heapq import (heappush, heappop)
from src.testutils import (contains_same_elements)

"""
Given two sorted arrays in descending order, find `k` pairs with the largest sum
where each pair consists of numbers from both arrays.
"""


def k_pairs_largest_sums(l1, l2, k):
    """
    Time Complexity:  O(k^2 * log k)
    Space Complexity: O(k)
    """
    min_heap = []

    # You only need to make pairs with at most the first `k` items from both arrays.
    for i in range(0, min(len(l1), k)):
        for j in range(0, min(len(l2), k)):
            if len(min_heap) < k:
                heappush(min_heap, (l1[i] + l2[j], i, j))
            elif l1[i] + l2[j] < min_heap[0][0]:
                # Once you find a pair that is smaller than the smallest pair,
                # then you know you can't find anything bigger.
                break
            else:
                heappop(min_heap)
                heappush(min_heap, (l1[i] + l2[j], i, j))

    result = []
    for _, i, j in min_heap:
        result.append([l1[i], l2[j]])

    return result


def test_ex1():
    l1 = [9, 8, 2]
    l2 = [6, 3, 1]
    k = 3
    actual = k_pairs_largest_sums(l1, l2, k)
    expected = [[9, 3], [9, 6], [8, 6]]
    assert contains_same_elements(actual, expected)


def test_ex2():
    l1 = [5, 2, 1]
    l2 = [2, -1]
    k = 3
    actual = k_pairs_largest_sums(l1, l2, k)
    expected = [[5, 2], [5, -1], [2, 2]]
    assert contains_same_elements(actual, expected)
