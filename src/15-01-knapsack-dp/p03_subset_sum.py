"""
Given a set of positive numbers, determine if a subset exists whose sum is equal
to the given number `s`.
"""


def subset_sum_bf(nums, s):
    """
    Time Complexity:  O(2^n)
    Space Complexity: O(n)
    """
    def recursive(nums, s, i):
        if s == 0:
            return True

        if i >= len(nums) or len(nums) < 1:
            return False

        take = False
        if nums[i] <= s:
            take = recursive(nums, s - nums[i], i + 1)

        return take or recursive(nums, s, i + 1)

    return recursive(nums, s, 0)


def subset_sum_td(nums, s):
    """
    Time Complexity:  O(n * s)
    Space Complexity: O(n * s)
    """
    if len(nums) < 1:
        return False

    def recursive(nums, s, i, memo):
        if i >= len(nums):
            return False

        if memo[i][s] is not None:
            return memo[i][s]

        if s == 0:
            memo[i][s] = True
        else:
            take = False
            if nums[i] <= s:
                take = recursive(nums, s - nums[i], i + 1, memo)

            memo[i][s] = take or recursive(nums, s, i + 1, memo)

        return memo[i][s]

    memo = [[None for _ in range(s + 1)] for _ in range(len(nums))]
    return recursive(nums, s, 0, memo)


def subset_sum_bu(nums, sum):
    """
    Time Complexity:  O(n * s)
    Space Complexity: O(n * s)
    """
    if len(nums) < 1:
        return False

    table = [[None for _ in range(sum + 1)] for _ in range(len(nums))]

    # If the sum is 0, then the sum has arbitrarily been met with a empty set.
    for i in range(len(nums)):
        table[i][0] = True

    # If we are only considering a single element, then the subset sum can only
    # be reached if it is equal to this element.
    for s in range(1, sum + 1):
        table[0][s] = nums[0] == s

    # Iterate through the remaining sub-problems in the table.
    for i in range(1, len(nums)):
        for s in range(1, sum + 1):
            take = False
            if nums[i] <= s:
                take = table[i - 1][s - nums[i]]
            table[i][s] = take or table[i - 1][s]

    return table[len(nums) - 1][sum]


def test_bf1():
    nums = [1, 2, 3, 7]
    s = 6
    actual = subset_sum_bf(nums, s)
    expected = True


def test_bf2():
    nums = [1, 2, 7, 1, 5]
    s = 10
    actual = subset_sum_bf(nums, s)
    expected = True


def test_bf3():
    nums = [1, 3, 4, 8]
    s = 6
    actual = subset_sum_bf(nums, s)
    expected = False


def test_td1():
    nums = [1, 2, 3, 7]
    s = 6
    actual = subset_sum_td(nums, s)
    expected = True


def test_td2():
    nums = [1, 2, 7, 1, 5]
    s = 10
    actual = subset_sum_td(nums, s)
    expected = True


def test_td3():
    nums = [1, 3, 4, 8]
    s = 6
    actual = subset_sum_td(nums, s)
    expected = False


def test_bu1():
    nums = [1, 2, 3, 7]
    s = 6
    actual = subset_sum_bu(nums, s)
    expected = True


def test_bu2():
    nums = [1, 2, 7, 1, 5]
    s = 10
    actual = subset_sum_bu(nums, s)
    expected = True


def test_bu3():
    nums = [1, 3, 4, 8]
    s = 6
    actual = subset_sum_bu(nums, s)
    expected = False
