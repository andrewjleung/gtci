"""
Given the weights and profits of `n` items, we are asked to put these items in a
knapsack with a capacity `c`. The goal is to get the maximum profit out of the
knapsack items. Each item can only be selected once, as we don't have multiple
quantities of any item.
"""


def knapsack_brute_force(weights, profits, capacity):
    """
    Time Complexity:  O(2^n)
        - For each item, there are two decisions. Pick or not pick.
    Space Complexity: O(n) 
        - The depth of the recursive call tree is `n`.
    """
    def recursive(i, weights, profits, capacity):
        # Base case.
        if capacity <= 0 or i >= len(weights):
            return 0

        pick_profit = 0
        if weights[i] <= capacity:
            pick_profit = profits[i] + recursive(
                i + 1, weights, profits, capacity - weights[i])

        not_pick_profit = recursive(i + 1, weights, profits, capacity)

        # Compare the profit of both options, to pick or not to pick.
        return max(pick_profit, not_pick_profit)

    return recursive(0, weights, profits, capacity)


def knapsack_top_down(weights, profits, capacity):
    """
    Time Complexity:  O(n * c)
        - `c` is the capacity of the knapsack.
        - `n` is the number of elements.
    Space Complexity: O(n * c)
        - To store the memo.
        - There is also O(n) space needed for the recursive call stack, but that
          is lost asymptotically.
    """
    # Create the memo, initializing every cell with -1.
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(len(weights))]

    def recursive(memo, i, weights, profits, capacity):
        # Base case.
        if capacity <= 0 or i >= len(weights):
            return 0

        # Check if the memo contains the answer already.
        if memo[i][capacity] != -1:
            return memo[i][capacity]

        pick_profit = 0
        if weights[i] <= capacity:
            pick_profit = profits[i] + \
                recursive(memo, i + 1, weights, profits, capacity - weights[i])

        not_pick_profit = recursive(memo, i + 1, weights, profits, capacity)

        # Set the value in the memo.
        memo[i][capacity] = max(pick_profit, not_pick_profit)
        return memo[i][capacity]

    return recursive(memo, 0, weights, profits, capacity)


def get_selection(table, weights, profits, capacity):
    selection = []
    i = len(weights) - 1
    profit = table[i][capacity]

    # Go through each element and determine if that element was picked.
    # An element was picked if the cell above the current position in the
    # traversal of the table is not the same as the current position's value.
    # This is because there are no items with 0 profit, meaning that the the
    # cell above being the same as the current cell implies that the item wasn't
    # picked. Otherwise it was.
    for i in range(len(weights) - 1, 0, -1):
        if table[i - 1][capacity] != profit:
            selection.append(i)
            capacity -= weights[i]
            profit -= profits[i]

    if profit != 0:
        selection.append(0)

    return selection


def knapsack_bottom_up(weights, profits, capacity):
    """
    Time Complexity:  O(n * c)
    Space Complexity: O(n * c)
    """
    n = len(weights)

    # Base cases / error checks.
    if capacity <= 0 or n <= 0 or len(profits) != n:
        return 0

    # Initialize the table with 0s. This is what we'll be building up.
    # Here, `i` (rows) represents the inclusive upper bound index on the range
    # of elements to pick we are considering for that particular sub-problem.
    # `c` represents the capacity we have in the knapsack.
    table = [[0 for _ in range(capacity + 1)] for _ in range(n)]

    # This step is redundant because of initialization, but important to point
    # out nevertheless. If you have no capacity, then you can't pick anything
    # and therefore have no profit.
    for i in range(n):
        table[i][0] = 0

    # Initialize the first row of the table i.e. i = 0. The only decision is to
    # take the element if you can, there are no sub-problems since there are no
    # other elements to pick.
    for c in range(capacity + 1):
        if weights[0] <= c:
            table[0][c] = profits[0]

    # Fill the rest of the table in. At each cell, you can either choose to pick
    # the element at `i` if you can, or not pick it. Not picking it defers to
    # the cell in the row below with the same capacity. Picking it defers to the
    # row below with the weight of the element at `i` subtracted from the
    # capacity.
    for i in range(1, n):
        for c in range(1, capacity + 1):
            not_pick_profit = table[i - 1][c]
            pick_profit = 0

            if weights[i] <= c:
                pick_profit = profits[i] + table[i - 1][c - weights[i]]

            table[i][c] = max(not_pick_profit, pick_profit)

    print(get_selection(table, weights, profits, capacity))

    return table[n - 1][capacity]


def knapsack_bottom_up_space_optimized(weights, profits, capacity):
    """
    Time Complexity:  O(n * c)
    Space Complexity: O(c)
    """
    n = len(weights)

    # Base cases / error checks.
    if capacity <= 0 or n <= 0 or len(profits) != n:
        return 0

    # You only need to keep track of the previous row in order to compute the
    # current row! Because of this we only need a single row.
    table = [0 for _ in range(capacity + 1)]
    table[0] = 0

    for c in range(capacity + 1):
        if weights[0] <= c:
            table[c] = profits[0]

    for i in range(1, n):
        # Iterate through capacity backwards to avoid overwriting cells still
        # required to calculate later ones.
        for c in range(capacity, -1, -1):
            not_pick_profit = table[c]
            pick_profit = 0

            if weights[i] <= c:
                pick_profit = profits[i] + table[c - weights[i]]

            table[c] = max(not_pick_profit, pick_profit)

    return table[capacity]


weights = [2, 3, 1, 4]
profits = [4, 5, 3, 7]
capacity = 5
expected = 10


def test_brute_force():
    actual = knapsack_brute_force(weights, profits, capacity)
    assert actual == expected


def test_top_down():
    actual = knapsack_top_down(weights, profits, capacity)
    assert actual == expected


def test_bottom_up():
    actual = knapsack_bottom_up(weights, profits, capacity)
    assert actual == expected


def test_bottom_up_space_optimized():
    actual = knapsack_bottom_up_space_optimized(weights, profits, capacity)
    assert actual == expected
