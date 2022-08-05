from heapq import (heappush, heappop)

"""
Given an array of numbers and a number `k`, we need to remove `k` numbers from
the array such that we are left with maximum distinct numbers
"""

# We want to prioritize numbers with a frequency greater than 1 that will take
# the fewest removals to get to one occurrence.


def max_distinct_elements(nums, k):
    """
    Time Complexity:  O(n + n * log n + k * log n)
    Space Complexity: O(n)
    """
    # Edge case. You'd have to remove all the items.
    if len(nums) <= k:
        return 0

    # Find the frequencies of all the numbers.
    frequencies = {}  # O(n) elements
    for num in nums:  # O(n) iterations
        frequencies[num] = frequencies.get(num, 0) + 1

    # Add all numbers with frequency > 1 to a min heap based on the difference
    # between their frequency and 1. Add all other distinct numbers to a results
    # array.
    distinct_elements = 0
    min_heap = []  # O(n) elements

    for num, freq in frequencies.items():  # O(n) iterations
        if freq < 2:
            distinct_elements += 1
        else:
            heappush(min_heap, (freq - 1, num))  # O(log n)

    # Pop off numbers from the heap, making them distinct and adding them to the
    # results array until `k` elements have been removed.
    while k > 0 and len(min_heap) > 0:  # O(k) iterations
        (copies_to_remove, num) = heappop(min_heap)  # O(log n)
        k -= copies_to_remove

        if k >= 0:
            distinct_elements += 1

    # Return the length of the results array. There may still be remaining
    # elements to remove, meaning that we need to remove some distinct elements.
    # Note that `k` may be negative at this point, and we should only subtract
    # it if it's positive.
    return distinct_elements - max(k, 0)


def test_ex1():
    nums = [7, 3, 5, 8, 5, 3, 3]
    k = 2
    actual = max_distinct_elements(nums, k)
    expected = 3
    assert actual == expected


def test_ex2():
    nums = [3, 5, 12, 11, 12]
    k = 3
    actual = max_distinct_elements(nums, k)
    expected = 2
    assert actual == expected


def test_ex3():
    nums = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]
    k = 2
    actual = max_distinct_elements(nums, k)
    expected = 3
    assert actual == expected
