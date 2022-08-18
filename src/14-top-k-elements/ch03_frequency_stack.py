import pytest
from heapq import (heappush, heappop)

"""
Design a class that simulates a Stack data structure, implementing the following
two operations:

1. `push(int num)`: pushes the number `num` onto the stack.
2. `pop()`: returns the most frequent number on the stack. If there is a tie,
   return the number which was pushed later.
"""

"""
- We want to be able to find the index of an item in the heap in at most 
  logarithmic time.
"""


class Element:
    def __init__(self, number, frequency, sequence_num):
        self.number = number
        self.frequency = frequency
        self.sequence_num = sequence_num

    def __lt__(self, other):
        # First test frequency, then test sequence number to break ties.
        if self.frequency != other.frequency:
            # This is used for a max heap, so we use > instead.
            return self.frequency > other.frequency

        # Otherwise defer to sequence number.
        return self.sequence_num > other.sequence_num


class FrequencyStack:
    """
    Space Complexity: O(n)
    """

    def __init__(self):
        # This holds the frequency of each element in the heap at any given
        # point. Elements also hold their frequency at the time of their
        # insertion. There is no need to update frequency for each of them
        # because the later inserted element should always be popped first.
        self.frequencies = {}

        # This is used to keep track of the most frequent element at any given
        # point so that it can be removed. All elements, including duplicates,
        # are separately stored in the heap.
        self.max_heap = []

        # This is used to break ties. It is incremented for every element
        # inserted.
        self.sequence_num = 0

    def push(self, num):
        """
        Time Complexity:  O(log n)
        """
        # Increment the frequency of the number.
        self.frequencies[num] = self.frequencies.get(num, 0) + 1

        # Add the element ot the heap.
        heappush(self.max_heap, Element(
            num, self.frequencies[num], self.sequence_num))

        # Increment the sequence number.
        self.sequence_num += 1

    def pop(self):
        """
        Time Complexity:  O(log n)
        """
        # Remove the root of the heap.
        number = heappop(self.max_heap).number

        # Decrement the element's frequency.
        self.frequencies[number] -= 1

        if self.frequencies[number] == 0:
            del self.frequencies[number]

        return number


def test_ex():
    fs = FrequencyStack()

    with pytest.raises(IndexError) as e_info:
        fs.pop()

    fs.push(1)
    fs.push(2)
    fs.push(3)
    fs.push(2)
    fs.push(1)
    fs.push(2)
    fs.push(5)

    assert fs.pop() == 2
    assert fs.pop() == 1
    assert fs.pop() == 2
