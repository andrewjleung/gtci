"""
Given a set of positive numbers, find the total number of subsets whose sum is
equal to a given number `s`.
"""


def count_of_subset_sum_bf(nums, s):
    """
    Time Complexity:  O(2^n)
    Space Complexity: O(n)
    """
    def recursive(nums, s, i):
        if s == 0:
            # There is only a single subset with a sum of 0, given that there
            # are only positive numbers in the set. This is the empty subset.
            return 1

        if i >= len(nums):
            # You cannot possibly have an empty subset which reaches a sum other
            # than 0. Thus, there are no possibilities of subsets.
            return 0

        # Count all subsets that reach the sum `s` that don't include `i`.
        not_include_count = recursive(nums, s, i + 1)

        # Count all the subsets that include `i`.
        include_count = 0
        if nums[i] <= s:
            include_count = recursive(nums, s - nums[i], i + 1)

        return not_include_count + include_count

    return recursive(nums, s, 0)


def count_of_subset_sum_td(nums, s):
    """
    Time Complexity:  O(n * s)
    Space Complexity: O(n * s)
    """
    def recursive(nums, s, i, memo):
        if s == 0:
            # There is only a single subset with a sum of 0, given that there
            # are only positive numbers in the set. This is the empty subset.
            return 1

        if i >= len(nums):
            # You cannot possibly have an empty subset which reaches a sum other
            # than 0. Thus, there are no possibilities of subsets.
            return 0

        if memo[i][s] != -1:
            return memo[i][s]

        # Count all subsets that reach the sum `s` that don't include `i`.
        not_include_count = recursive(nums, s, i + 1, memo)

        # Count all the subsets that include `i`.
        include_count = 0
        if nums[i] <= s:
            include_count = recursive(nums, s - nums[i], i + 1, memo)

        memo[i][s] = not_include_count + include_count
        return memo[i][s]

    memo = [[-1 for _ in range(s + 1)] for _ in range(len(nums))]
    return recursive(nums, s, 0, memo)


def count_of_subset_sum_bu(nums, s):
    """
    Time Complexity:  O(n * s)
    Space Complexity: O(s)
    """
    n = len(nums)
    # Rather than filling in an entire `n * s` table, we can improve our space
    # complexity by realizing that every problem only depends on sub-problems
    # from the previous row (`i - 1`) rather than the entire table. We can just
    # update the row in place for each `i`. However, since each problem also
    # depends on smaller sums (the values of which may vary), we can't fill in
    # columns of increasing sum. This will overwrite cells which we need to
    # calculate later cells in the row. Therefore, we iterate through sums in
    # decreasing order in the final loop.
    table = [0 for _ in range(s + 1)]

    # For all `i`, there is only a single subset with a sum of 0, that being the
    # empty set since the set of numbers is constrained to positive numbers.
    table[0] = 1

    # For all `s`, if there is only a single element, the only way for there to
    # be a subset sum of `s` is if that single element is equal to `s`.
    # Otherwise, there are no subsets.
    for sum in range(1, s + 1):
        if sum == nums[0]:
            table[sum] = 1
        else:
            table[sum] = 0

    # Fill in the rest of the table.
    for i in range(1, n):
        # Iterate through sums backwards to prevent overwriting cells that we
        # still need while calculating this current row.
        for sum in range(s, -1, -1):
            if nums[i] <= sum:
                table[sum] += table[sum - nums[i]]

    return table[s]


def test_bf1():
    nums = [1, 1, 2, 3]
    s = 4
    actual = count_of_subset_sum_bf(nums, s)
    expected = 3
    assert actual == expected


def test_bf2():
    nums = [1, 2, 7, 1, 5]
    s = 9
    actual = count_of_subset_sum_bf(nums, s)
    expected = 3
    assert actual == expected


def test_td1():
    nums = [1, 1, 2, 3]
    s = 4
    actual = count_of_subset_sum_td(nums, s)
    expected = 3
    assert actual == expected


def test_td2():
    nums = [1, 2, 7, 1, 5]
    s = 9
    actual = count_of_subset_sum_td(nums, s)
    expected = 3
    assert actual == expected


def test_bu1():
    nums = [1, 1, 2, 3]
    s = 4
    actual = count_of_subset_sum_bu(nums, s)
    expected = 3
    assert actual == expected


def test_bu2():
    nums = [1, 2, 7, 1, 5]
    s = 9
    actual = count_of_subset_sum_bu(nums, s)
    expected = 3
    assert actual == expected
