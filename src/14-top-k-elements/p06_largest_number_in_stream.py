from heapq import (heappush, heappop)

"""
Design a class to efficiently find the Kth largest element in a stream of
numbers.

The class should have the following two things:

1. The constructor of the class should accept an integer array containing 
initial numbers from the stream and an integer `k`.
2. The class should expose a function `add(int num)` which will store the given
number and return the Kth largest number.
"""

"""
Space Complexity: O(k)
"""


class KthLargest:
    def __init__(self, nums, k):
        """
        Time Complexity:  O(n * log k)
        """
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, num):
        """
        Time Complexity:  O(log k)
        """
        heappush(self.min_heap, num)

        # If the heap has become larger than `k`, remove the smallest number.
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)

        return self.min_heap[0]


def test_ex1():
    nums = [3, 1, 5, 12, 2, 11]
    k = 4
    kthLargest = KthLargest(nums, k)
    assert kthLargest.add(6) == 5
    assert kthLargest.add(13) == 6
    assert kthLargest.add(4) == 6
