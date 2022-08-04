from heapq import (heappush, heappop)
from collections import deque

"""
Given a sorted number array and two integers `k` and `x`, find `k` closest
numbers to `x` in the array. Return the numbers in sorted order. `x` is not
necessarily present in the array.
"""


def dist_from_x(num, x):
    return abs(num - x)


def binary_search(nums, k):
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = start + (end - start) // 2

        if nums[middle] == k:
            return middle

        if k < nums[middle]:
            end = middle - 1
        else:
            start = middle + 1

    # If `start` is 0, then `k` is smaller than all the elements since `end` was
    # decremented at the very last iteration, also being 0.
    if start == 0:
        return start

    # If start is not 0, `k` is between `end` and `start`. Return `end` as the
    # number right before `k` if `k` was present.
    return end


def k_closest_numbers_heap(nums, k, x):
    """
    Time Complexity:  O(log n + k * log k)
    Space Complexity: O(k)
    """
    # Search for the closest number to `x`.
    closest = binary_search(nums, x)  # O(log n)
    low = max(closest - k, 0)
    high = min(closest + k, len(nums) - 1)

    min_heap = []

    # Given that the array is sorted, the other closest numbers to `x` must be
    # within `k` places of the closest. Look through each of these numbers,
    # sorting them by closeness using a min heap.
    for i in range(low, high + 1):  # O(k) iterations
        heappush(min_heap, (dist_from_x(nums[i], x), nums[i]))  # O(log k)

    # Get the `k` closest elements from the heap.
    results = []
    for _ in range(k):  # O(k) iterations
        results.append(heappop(min_heap)[1])  # O(log k)

    # The heap is sorted by closeness, not the numbers themselves.
    # The final result must be sorted, so we sort here.
    results.sort()  # O(k * log k)
    return results

# Two pointer approach.


def k_closest_numbers(nums, k, x):
    """
    Time Complexity:  O(k + log n)
    Space Complexity: O(k)
    """
    # Search for the closest number to `x`.
    closest = binary_search(nums, x)  # O(log n)

    results = deque()

    # Binary search will yield `k`'s index if found or the number which would
    # come right below `k` if `k` was present.
    left = closest
    right = closest + 1

    for i in range(k):  # O(k)
        # Both sides are valid so compare them and add the closer one.
        if left >= 0 and right < len(nums):
            left_dist = dist_from_x(nums[left], x)
            right_dist = dist_from_x(nums[right], x)

            if left_dist <= right_dist:
                results.appendleft(nums[left])
                left -= 1
            else:
                results.append(nums[right])
                right += 1
        # The right side is past the end of the array. Take the left.
        elif left >= 0:
            results.appendleft(nums[left])
            left -= 1
        # The left side is past the end of the array. Take the right.
        else:
            result.append(nums[right])
            right += 1

    return list(results)


def test_ex1():
    nums = [5, 6, 7, 8, 9]
    k = 3
    x = 7
    actual = k_closest_numbers(nums, k, x)
    expected = [6, 7, 8]
    assert actual == expected


def test_ex2():
    nums = [2, 4, 5, 6, 9]
    k = 3
    x = 6
    actual = k_closest_numbers(nums, k, x)
    expected = [4, 5, 6]
    assert actual == expected


def test_ex3():
    nums = [2, 4, 5, 6, 9]
    k = 3
    x = 10
    actual = k_closest_numbers(nums, k, x)
    expected = [5, 6, 9]
    assert actual == expected
