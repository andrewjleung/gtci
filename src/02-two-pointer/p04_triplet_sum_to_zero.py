"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero
"""


def triplet_sum_zero(arr):
    """
    Time Complexity:  O(n^2)
    Space Complexity: O(n)
    """
    # Sort the array in order to make use of the previous target sum algorithm.
    arr.sort()

    # Results accumulator.
    triplets = []

    for i in range(len(arr)):
        # Skip duplicate elements.
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        search_pair(arr, -arr[i], i + 1, triplets)

    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1

    # Scan from subarray (left to the end) for solutions.
    while left < right:
        current_sum = arr[left] + arr[right]
        # A solution has been found, note it down and check for more solutions.
        if current_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1

            # Increment the left and right pointers to the next non-duplicate element.
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right += 1
        elif target_sum > current_sum:
            left += 1
        else:
            right -= 1


def test_ex1():
    arr = [-3, 0, 1, 2, -1, 1, -2]
    o = [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    assert triplet_sum_zero(arr) == o


def test_ex2():
    arr = [-5, 2, -1, -2, 3]
    o = [[-5, 2, 3], [-2, -1, 3]]
    assert triplet_sum_zero(arr) == o
