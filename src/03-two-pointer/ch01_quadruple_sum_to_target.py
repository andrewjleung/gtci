"""
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum
is equal to the target number.
"""


def quadruple_sum(arr, t):
    """
    Time Complexity:  O(n^3)
    Space Complexity: O(n)
    """
    arr.sort()
    results = []

    for i in range(len(arr)):
        # Skip duplicate elements.
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        results += search_triplet(i, arr, t, i + 1)

    return results


def search_triplet(fourth, arr, t, low):
    results = []

    for i in range(low, len(arr)):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[fourth] + arr[i] + arr[left] + arr[right]

            if current_sum == t:
                results.append([arr[fourth], arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif current_sum < t:
                left += 1
            else:
                right -= 1

    return results


def test_ex1():
    arr = [4, 1, 2, -1, 1, -3]
    t = 1
    o = [[-3, -1, 1, 4], [-3, 1, 1, 2]]
    assert quadruple_sum(arr, t) == o


def test_ex2():
    arr = [2, 0, -1, 1, -2, 2]
    t = 2
    o = [[-2, 0, 2, 2], [-1, 0, 1, 2]]
    assert quadruple_sum(arr, t) == o
