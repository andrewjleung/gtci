"""
Given an unsorted array containing numbers and a number `k`, find the first `k` missing positive
numbers in the array.
"""


def find_k_missing_pos(nums, k):
    """
    Time Complexity:  O(n + k)
    Space Complexity: O(k)
    """
    i = 0
    # Numbers that are greater or equal to the length of the array which appear within the array.
    # These need to be accumulated so they can later be ignored when building up the array of
    # missing positives.
    greater_positives = set()

    while i < len(nums):
        j = nums[i] - 1

        if nums[i] > len(nums):
            greater_positives.add(nums[i])
            i += 1
            continue

        if nums[i] < 1 or nums[i] == nums[j]:
            i += 1
            continue

        nums[i], nums[j] = nums[j], nums[i]

    results = []
    i = 0

    while len(results) < k:
        # Ignore numbers within the array which are in the right place.
        if i < len(nums) and nums[i] - 1 == i:
            i += 1
            continue

        # Add missing numbers which aren't within the array at the wrong position.
        if i + 1 not in greater_positives:
            results.append(i + 1)
        i += 1

    return results


def test_ex1():
    nums = [3, -1, 4, 5, 5]
    k = 3
    actual = find_k_missing_pos(nums, k)
    assert actual == [1, 2, 6]


def test_ex2():
    nums = [2, 3, 4]
    k = 3
    actual = find_k_missing_pos(nums, k)
    assert actual == [1, 5, 6]


def test_ex3():
    nums = [-2, -3, 4]
    k = 2
    actual = find_k_missing_pos(nums, k)
    assert actual == [1, 2]


def test_ex4():
    nums = [1, 2, 3, 4]
    k = 3
    actual = find_k_missing_pos(nums, k)
    assert actual == [5, 6, 7]


def test_ex5():
    nums = [1, 4]
    k = 4
    actual = find_k_missing_pos(nums, k)
    assert actual == [2, 3, 5, 6]
