"""
You are given a set of positive numbers and a target sum `s`. Each number should
be assigned either a `+` or a `-` sign. We need to find the total way to assign
symbols to make the sum of the numbers equal to the target `s`.
"""

"""
The intuition of this problem that lets you reduce it to finding a subset sum is
that after assigning each number a sign, you can take all positive numbers and
put them on one side and all negative numbers and put them on another side.
Then, you can factor out a `-1` from the side containing all the negative 
numbers. This leaves you with the solution being expressed in terms of the
difference of two subset sums.

For instance, take the solution `1 - 1 - 2 + 3`. Separating out the positives 
and negatives, you get `1 + 3 - 1 - 2`. These are identical because there are no
parentheses involved. Factoring out a `-1` from the negatives you get 
`1 + 3 - (1 + 2)` or `(1 + 3) - (1 + 2)`. You can do something like this for 
every solution, meaning that finding a solution is equivalent to finding two
subsets such that their difference is the target sum: `sum(s1) - sum(s2) = t`.

Then, knowing that the sum of both subset sums must be the total sum of the set
of numbers, you can eliminate `s2` from the equation by adding 
`S = sum(s1) + sum(s2)` to both sides, getting `2 * sum(s1) = t + S`. Then you
can reduce to a subset sum problem by solving for `sum(s1)`:
`sum(s1) = (t + S) / 2`.
"""


def target_sum_bf(nums, s):
    """
    Time Complexity:  O(2^n)
    Space Complexity: O(n)
    """
    def recursive(nums, s, i):
        if s == 0:
            return 1

        if i >= len(nums):
            return 0

        take = 0
        if nums[i] <= s:
            take = recursive(nums, s - nums[i], i + 1)
        return take + recursive(nums, s, i + 1)

    total_sum = sum(nums)

    # If the total sum is less than `s`, then there is no way to possibly reach
    # `s` even with all positive numbers. The same goes for if the total sum
    # plus `s` is odd.
    if total_sum < s or (s + total_sum) % 2 == 1:
        return 0

    return recursive(nums, (s + sum(nums)) // 2, 0)


def target_sum_td(nums, s):
    """
    Time Complexity:  O(n * s)
        - I'm not sure about this being in terms of `s` since it's moreso in
          in terms of `s` plus the sum of all the numbers which you could say is
          O(n).
    Space Complexity: O(n * s)
    """
    def recursive(nums, s, i, memo):
        if s == 0:
            return 1

        if i >= len(nums):
            return 0

        if memo[i][s] != -1:
            return memo[i][s]

        take = 0
        if nums[i] <= s:
            take = recursive(nums, s - nums[i], i + 1, memo)
        memo[i][s] = take + recursive(nums, s, i + 1, memo)
        return memo[i][s]

    total_sum = sum(nums)

    if total_sum < s or (s + total_sum) % 2 == 1:
        return 0

    target = (s + sum(nums)) // 2
    memo = [[-1 for _ in range(target + 1)] for _ in range(len(nums))]
    return recursive(nums, target, 0, memo)


def target_sum_bu(nums, s):
    """
    Time Complexity:  O(n * s)
    Space Complexity: O(s)
    """
    n = len(nums)
    total_sum = sum(nums)

    if total_sum < s or (s + total_sum) % 2 == 1:
        return 0

    target = (s + sum(nums)) // 2
    row = [-1 for _ in range(target + 1)]

    # There will always be a solution (the empty set) for a target sum of 0.
    row[0] = 1

    # Establish the rest of the first row (i = 0). The subset sum can only equal
    # to the non-zero target if the single element at `i` equals the target.
    for s in range(1, target + 1):
        row[s] = 1 if nums[0] == s else 0

    # Iterate through the remaining sub-problems.
    for i in range(1, n):
        for s in range(target, 0, -1):
            if nums[i] <= s:
                row[s] += row[s - nums[i]]

    return row[target]


def test_bf1():
    nums = [1, 1, 2, 3]
    s = 1
    actual = target_sum_bf(nums, s)
    expected = 3
    assert actual == expected


def test_bf2():
    nums = [1, 2, 7, 1]
    s = 9
    actual = target_sum_bf(nums, s)
    expected = 2
    assert actual == expected


def test_td1():
    nums = [1, 1, 2, 3]
    s = 1
    actual = target_sum_td(nums, s)
    expected = 3
    assert actual == expected


def test_td2():
    nums = [1, 2, 7, 1]
    s = 9
    actual = target_sum_td(nums, s)
    expected = 2
    assert actual == expected


def test_bu1():
    nums = [1, 1, 2, 3]
    s = 1
    actual = target_sum_bu(nums, s)
    expected = 3
    assert actual == expected


def test_bu2():
    nums = [1, 2, 7, 1]
    s = 9
    actual = target_sum_bu(nums, s)
    expected = 2
    assert actual == expected
