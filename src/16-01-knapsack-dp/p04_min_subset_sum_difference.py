import math

"""
Given a set of positive numbers, partition the set into two subsets with minimum
difference between their subset sums.
"""


def min_subset_sum_bf(nums):
    """
    Time Complexity:  O(2^n)
    Space Complexity: O(n)
    """
    if len(nums) < 1:
        return 0

    def recursive(nums, i, sum1, sum2):
        if i >= len(nums):
            return abs(sum2 - sum1)

        # Find the minimum difference when putting the number into subset 1.
        put_in_1_min = recursive(nums, i + 1, sum1 + nums[i], sum2)

        # The minimum difference can't get any smaller than 0, so if the first
        # subtree already evaluated to 0, we don't need to evaluate the second
        # subtree.
        if put_in_1_min > 0:
            return min(recursive(nums, i + 1, sum1, sum2 + nums[i]), put_in_1_min)

        return put_in_1_min

    return recursive(nums, 0, 0, 0)


def min_subset_sum_td(nums):
    """
    Time Complexity:  O(n * s)
    Space Complexity: O(n * s)
    """
    if len(nums) < 1:
        return 0

    def recursive(nums, i, sum1, sum2, memo):
        if i >= len(nums):
            return abs(sum2 - sum1)

        if memo[i][sum1] is not None:
            return memo[i][sum1]

        # Find the minimum difference when putting the number into subset 1.
        put_in_1_min = recursive(nums, i + 1, sum1 + nums[i], sum2, memo)

        # The minimum difference can't get any smaller than 0, so if the first
        # subtree already evaluated to 0, we don't need to evaluate the second
        # subtree.
        if put_in_1_min > 0:
            memo[i][sum1] = min(
                recursive(nums, i + 1, sum1, sum2 + nums[i], memo), put_in_1_min)
        else:
            memo[i][sum1] = put_in_1_min

        return memo[i][sum1]

    # Just the current index and `sum1` are enough to uniquely identify a
    # sub-problem. This is because it is impossible to have two sub-problems
    # with the same `i` and `sum1` and different values for `sum2`. `sum2` must
    # always equal the total across all numbers [0, i) minus `sum1`.
    memo = [[None for _ in range(sum(nums) + 1)] for _ in range(len(nums))]
    return recursive(nums, 0, 0, 0, memo)


# Using the same algorithm as the other problems will complicate the bottom up
# approach making it harder to fill in the base cases. Where in top-down DP `i`
# represents simply what element we are currently making a decision on, in
# bottom up DP it represents "only considering elements up to `i`." What does it
# then mean to have a sub-problem with `i = 0` and `sum1 = 0`? You can't figure
# this out without knowing `sum2` but what is `sum2` at that point?
#
# Instead of trying to answer this question, we simplify the problem to instead
# trying to get a subset sum as close as possible to half of the total sum of
# all the numbers.
#
# An alternative to this is to instead just compute whether or not you can get
# a subset sum of half the total sum. When the full table is filled, the largest
# sum in the last row (considering all elements) represents the closest subset
# sum you can get to half, which you can then use to calculate the other
# subset's total and get the difference.
def min_subset_sum_bu1(nums):
    """
    Time Complexity:  O(n * s)
    Space Complexity: O(n * s)
    """
    if len(nums) < 1:
        return 0

    total = sum(nums)
    half = total // 2
    table = [[None for _ in range(half + 1)] for _ in range(len(nums))]

    # Fill in base cases for when `subset_sum` is 0. In this case, the sum has
    # already been met by an empty set. The closest we've gotten to the target
    # subset sum is 0.
    for i in range(len(nums)):
        table[i][0] = 0

    # Fill in base cases for when you are only considering a single element i.e.
    # i = 0. In this case, the closest we can get to the target subset sum is by
    # taking the first value if we can.
    for s in range(1, half + 1):
        if nums[0] <= s:
            table[0][s] = s - nums[0]
        else:
            table[0][s] = s

    # Fill in the remaining cells in the table.
    for i in range(1, len(nums)):
        for s in range(1, half + 1):
            not_pick = table[i - 1][s]

            # If you can take the current number in the subset, then the minimum
            # difference from the target subset sum is the minimum of both
            # sub-problems for either taking the current number or not taking
            # it.
            if nums[i] <= s:
                pick = table[i - 1][s - nums[i]]
                table[i][s] = min(pick, not_pick)
            # If you can't take the current number in the subset, then you have
            # to skip it.
            else:
                table[i][s] = not_pick

    min_difference_from_half = table[len(nums) - 1][half]
    subset_sum1 = half - min_difference_from_half
    subset_sum2 = total - subset_sum1
    return subset_sum2 - subset_sum1


def min_subset_sum_bu2(nums):
    """
    Time Complexity:  O(n * s)
    Space Complexity: O(n * s)
    """
    if len(nums) < 1:
        return 0

    total = sum(nums)
    half = total // 2
    table = [[False for _ in range(half + 1)] for _ in range(len(nums))]

    # Fill in base cases for when `subset_sum` is 0. In this case, the sum has
    # already been met by an empty set.
    for i in range(len(nums)):
        table[i][0] = True

    # Fill in base cases for when you are only considering a single element i.e.
    # i = 0. In this case, we can only reach the subset sum if the number is
    # equal to the sum.
    for s in range(1, half + 1):
        table[0][s] = s == nums[0]

    # Fill in the remaining cells in the table.
    for i in range(1, len(nums)):
        for s in range(1, half + 1):
            not_pick = table[i - 1][s]
            pick = nums[i] <= s and table[i - 1][s - nums[i]]
            table[i][s] = pick or not_pick

    sum1 = 0
    for s in range(half, -1, -1):
        if table[len(nums) - 1][s]:
            sum1 = s
            break

    sum2 = total - sum1
    # `sum2` ≥ `sum1` because `sum1` is bound by half of the total.
    return sum2 - sum1


def test_bf1():
    nums = [1, 2, 3, 9]
    actual = min_subset_sum_bf(nums)
    expected = 3
    assert actual == expected


def test_bf2():
    nums = [1, 2, 7, 1, 5]
    actual = min_subset_sum_bf(nums)
    expected = 0
    assert actual == expected


def test_bf3():
    nums = [1, 3, 100, 4]
    actual = min_subset_sum_bf(nums)
    expected = 92
    assert actual == expected


def test_td1():
    nums = [1, 2, 3, 9]
    actual = min_subset_sum_td(nums)
    expected = 3
    assert actual == expected


def test_td2():
    nums = [1, 2, 7, 1, 5]
    actual = min_subset_sum_td(nums)
    expected = 0
    assert actual == expected


def test_td3():
    nums = [1, 3, 100, 4]
    actual = min_subset_sum_td(nums)
    expected = 92
    assert actual == expected


def test_bu1_1():
    nums = [1, 2, 3, 9]
    actual = min_subset_sum_bu1(nums)
    expected = 3
    assert actual == expected


def test_bu1_2():
    nums = [1, 2, 7, 1, 5]
    actual = min_subset_sum_bu1(nums)
    expected = 0
    assert actual == expected


def test_bu1_3():
    nums = [1, 3, 100, 4]
    actual = min_subset_sum_bu1(nums)
    expected = 92
    assert actual == expected


def test_bu2_1():
    nums = [1, 2, 3, 9]
    actual = min_subset_sum_bu2(nums)
    expected = 3
    assert actual == expected


def test_bu2_2():
    nums = [1, 2, 7, 1, 5]
    actual = min_subset_sum_bu2(nums)
    expected = 0
    assert actual == expected


def test_bu2_3():
    nums = [1, 3, 100, 4]
    actual = min_subset_sum_bu2(nums)
    expected = 92
    assert actual == expected
