from heapq import (heappush, heappop)

"""
Design a class to calculate the median of a number stream. The class should have the following two
methods:
1. `insertNum(int num)`: stores the number in the class.
2. `findMedian()`: returns the median of all numbers inserted in the class.

If the count of numbers inserted in the classis even, the median will be the average of the middle
two numbers.
"""


"""
Time Complexity:  O(logn) - heap insertion
Space Complexity: O(n) - the heaps
"""


class MedianOfAStream:
    def __init__(self):
        # Max-heap. Contains the lesser half of the stream.
        self.small_nums = []
        # Min-heap. Contains the greater half of the stream.
        self.large_nums = []

    def insert_num(self, num):
        # Place the number into a half depending on its relation to that half's topmost element.
        if len(self.small_nums) < 1 or num <= -self.small_nums[0]:
            heappush(self.small_nums, -num)
        else:
            heappush(self.large_nums, num)

        # Balance out the halves to an equal length.
        # In the case of an odd number of numbers, the max heap (smaller numbers) will be greater.
        if len(self.small_nums) > len(self.large_nums) + 1:
            heappush(self.large_nums, -heappop(self.small_nums))
        elif len(self.large_nums) > len(self.small_nums):
            heappush(self.small_nums, -heappop(self.large_nums))

    def find_median(self):
        # The halves are always balancing on insertion. If they aren't an equal length, this means
        # that there are an odd number of numbers and the lower half contains the extra, making that
        # element the median.
        if len(self.small_nums) != len(self.large_nums):
            return -self.small_nums[0]

        # There are an even number of elements. The median is the average of the greatest element of
        # the bottom half and the least element of the top half.
        return (-self.small_nums[0] + self.large_nums[0]) / 2.0


def test_ex1():
    sm = MedianOfAStream()
    sm.insert_num(3)
    sm.insert_num(1)
    assert sm.find_median() == 2
    sm.insert_num(5)
    assert sm.find_median() == 3
    sm.insert_num(4)
    assert sm.find_median() == 3.5
