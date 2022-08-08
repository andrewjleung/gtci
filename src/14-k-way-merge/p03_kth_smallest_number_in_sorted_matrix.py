from heapq import (heappush, heappop)

"""
Given an n * n matrix where each row and column is sorted in ascending order,
find the kth smallest element in the matrix.
"""


def kth_smallest_in_matrix_heap(matrix, k):
    """
    Time Complexity:  O(min(k, n) * log (min(k, n)) + k log n)
    Space Complexity: O(n)
    """
    min_heap = []

    # Since columns are also sorted, we only need to care about at most `k`
    # rows. If `k` is less than `n`, then the `k`th smallest element must be
    # either in the first row or the first column of the first `k` rows.
    for i in range(min(k, len(matrix))):  # O(min(k, n)) iterations
        heappush(min_heap, (matrix[i][0], matrix[i], 0))  # O(log (min(k, n)))

    number = None
    count = 1
    while len(min_heap) > 0:  # O(k) iterations
        number, l, i = heappop(min_heap)  # O(log n)

        if count == k:
            return number

        if i + 1 < len(l):
            heappush(min_heap, (l[i + 1], l, i + 1))  # O(log n)

        count += 1

    raise ValueError("k is bigger than the total number of elements.")


def count_smaller_or_eq(matrix, mid, smaller, larger):
    """
    Time Complexity:  O(n)
    """
    n = len(matrix)
    row = n - 1
    col = 0
    count = 0

    # The way this algorithm works to count the number of numbers less than or
    # equal to `mid` is by finding for each column the row at which the values
    # start becoming greater than `mid`. Alternatively, we are finding for each
    # row the column at which the values start becoming greater than `mid`.
    #
    # The algorithm also finds the largest value smaller than `mid` and the
    # smallest value larger than `mid` since these are required for the binary
    # search since we aren't partitioning based on index anymore, but rather by
    # value.
    while row >= 0 and col < n:  # O(n) iterations
        num = matrix[row][col]
        if mid < num:
            # If we see a number larger than `mid`, there's a chance it could be
            # the smallest number larger than `mid`.
            larger = min(larger, num)
            row -= 1
        else:
            # If we see a number less than or equal to `mid`, there's a chance
            # it could be the largest number less than or equal to `mid`.
            smaller = max(smaller, num)
            # If we know that the value in this columns is less than or equal
            # to `mid` (target), then we know that all values in this column
            # above this row are also less than or equal to `mid`. We can count
            # them into the total count.
            count += row + 1
            # We traverse to the next column to see if that number and by
            # extension column is also less than or equal to `mid`.
            col += 1

    return count, smaller, larger


def kth_smallest_in_matrix(matrix, k):
    """
    Time Complexity:  O(n * log(max, min))
        - We are doing a binary search not on indices, but rather the range of
          numbers within the matrix. This means that the domain of our search
          is the range of the numbers in the matrix, that being the largest 
          number minus the smallest number.
    Space Complexity: O(1)
    """
    n = len(matrix)
    start = matrix[0][0]
    end = matrix[n - 1][n - 1]

    while start < end:  # O(log(max, min))
        mid = start + (end - start) // 2
        smaller = matrix[0][0]
        larger = matrix[n - 1][n - 1]
        count, smaller, larger = count_smaller_or_eq(
            matrix, mid, smaller, larger)

        if count == k:
            return smaller

        if count < k:
            # The k'th number is in the upper range.
            start = larger
        else:
            # The k'the number is in the lower range.
            end = smaller

    return start


def test_ex1():
    matrix = [
        [2, 6, 8],
        [3, 7, 10],
        [5, 8, 11]
    ]
    k = 5
    actual = kth_smallest_in_matrix(matrix, k)
    expected = 7
    assert actual == expected
