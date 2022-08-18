from heapq import (heappush, heappop)
from src.testutils import (contains_same_elements, actual_in_expected)

"""
Given an unsorted array of numbers, find the top `K` frequently occurring 
numbers.
"""


def top_k_frequent_numbers(nums, k):
    """
    Time Complexity:  O(n + n * log k)
    Space Complexity: O(n + k)
    """
    frequencies = {}
    min_heap = []

    # Get the frequencies of each number.
    for num in nums:  # O(n)
        frequencies[num] = frequencies.get(num, 0) + 1

    # Insert `k` number-frequency pairs into the min heap, then insert
    # number-frequency pairs so long as they are replacing pairs with lesser
    # frequencies.
    i = 0
    for num, frequency in frequencies.items():  # O(n)
        if i < k:
            heappush(min_heap, (frequency, num))  # O(log k)
            i += 1
        else:
            if frequency > min_heap[0][0]:
                heappop(min_heap)  # O(log k)
                heappush(min_heap, (frequency, num))  # O(log k)

    return [pair[1] for pair in min_heap]  # O(k)


def test_ex1():
    nums = [1, 3, 5, 12, 11, 12, 11, 12, 11]
    k = 2
    actual = top_k_frequent_numbers(nums, k)
    expected = [12, 11]
    assert contains_same_elements(actual, expected)


def test_ex2():
    nums = [5, 12, 11, 3, 11]
    k = 2
    actual = top_k_frequent_numbers(nums, k)
    expected = [[11, 5], [11, 12], [11, 3]]
    assert actual_in_expected(actual, expected)
