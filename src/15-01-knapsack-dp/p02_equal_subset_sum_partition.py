"""
Given a set of positive numbers, find if we can partition it into two subsets
such that the sum of elements in both subsets is equal.
"""


def has_subset_sum(nums, s, i):
    if s == 0:
        return True

    # If there are no numbers whatsoever or we reach the end of the list of
    # numbers before finding a subset sum, then there is no partition.
    if len(nums) == 0 or i >= len(nums):
        return False

    take = False
    if nums[i] <= s:
        take = has_subset_sum(nums, s - nums[i], i + 1)

    return take or has_subset_sum(nums, s, i + 1)


def equal_subset_sum_partition_bf(nums):
    """
    Time Complexity:  O(2^n)
    Space Complexity: O(n)
    """
    total = sum(nums)

    if total % 2 != 0:
        return False

    return has_subset_sum(nums, total / 2, 0)


def has_subset_sum_td(nums, s, i, memo):
    if s == 0:
        return True

    if len(nums) == 0 or i >= len(nums):
        return False

    # Check if the answer has already been memoized.
    if memo[i][s] is not None:
        return memo[i][s]

    take = False
    if nums[i] <= s:
        take = has_subset_sum_td(nums, s - nums[i], i + 1, memo)

    # Memoize the answer.
    memo[i][s] = take or has_subset_sum_td(nums, s, i + 1, memo)
    return memo[i][s]


def equal_subset_sum_partition_td(nums):
    """
    Time Complexity:  O(n * s) - `s` is the sum of all the numbers.
    Space Complexity: O(n * s)
    """
    total = sum(nums)

    if total % 2 != 0:
        return False

    s = total // 2
    memo = [[None for _ in range(s + 1)] for _ in range(len(nums))]
    return has_subset_sum_td(nums, s, 0, memo)


def equal_subset_sum_partition_bu(nums):
    """
    Time Complexity:  O(n * s)
    Space Complexity: O(n * s)
    """
    total = sum(nums)

    if total % 2 != 0:
        return False

    half = total // 2
    table = [[False for _ in range(half + 1)] for _ in range(len(nums))]

    # If the sum is 0, then the subset sum has been reached and there is no need
    # to even consider further elements.
    for i in range(len(nums)):
        table[i][0] = True

    # If there is only a single element to consider, then the subset sum is only
    # reached if it is equal to the value of that single element.
    for s in range(1, half + 1):
        table[0][s] = s == nums[0]

    # Iterate through the remaining elements in the table and fill them in.
    for i in range(1, len(nums)):
        for s in range(1, half + 1):
            pick = False
            if nums[i] <= s:
                # If you pick the element to be in the subset, then you reduce
                # to the sub-problem considering all elements remaining except
                # this one, and a sum with the value of this element subtracted.
                pick = table[i - 1][s - nums[i]]

            # If you don't pick this element to be in the subset, then you
            # reduce to the sub-problem considering all elements remaining
            # except this one, and the same sum as before.
            table[i][s] = pick or table[i - 1][s]

    return table[len(nums) - 1][half]


def test_bf1():
    nums = [1, 2, 3, 4]
    actual = equal_subset_sum_partition_bf(nums)
    expected = True
    assert actual == expected


def test_bf2():
    nums = [1, 1, 3, 4, 7]
    actual = equal_subset_sum_partition_bf(nums)
    expected = True
    assert actual == expected


def test_bf3():
    nums = [2, 3, 4, 6]
    actual = equal_subset_sum_partition_bf(nums)
    expected = False
    assert actual == expected


def test_td1():
    nums = [1, 2, 3, 4]
    actual = equal_subset_sum_partition_td(nums)
    expected = True
    assert actual == expected


def test_td2():
    nums = [1, 1, 3, 4, 7]
    actual = equal_subset_sum_partition_td(nums)
    expected = True
    assert actual == expected


def test_td3():
    nums = [2, 3, 4, 6]
    actual = equal_subset_sum_partition_td(nums)
    expected = False
    assert actual == expected


def test_bu1():
    nums = [1, 2, 3, 4]
    actual = equal_subset_sum_partition_bu(nums)
    expected = True
    assert actual == expected


def test_bu2():
    nums = [1, 1, 3, 4, 7]
    actual = equal_subset_sum_partition_bu(nums)
    expected = True
    assert actual == expected


def test_bu3():
    nums = [2, 3, 4, 6]
    actual = equal_subset_sum_partition_bu(nums)
    expected = False
    assert actual == expected
