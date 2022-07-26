from heapq import (heappush, heappop)

"""
Given a set of investment projects with their respective profits, we need to find the most 
profitable project. We are given an initial capital and are allowed to invest only in a fixed
number of projects. Our goal is to choose projects that give us the maximum profit. Write a function
that returns the maximum total capital after selecting the most profitable projects.

We can start an investment project only when we have the required capital. Once a project is 
selected, we can assume that its profit has become our capital.
"""


def maximize_capital(capitals, profits, init_capital, num_projects):
    """
    Time Complexity:  O(nlogn + klogn)
    Space Complexity: O(n)
    """
    capital = init_capital
    capital_min_heap = []
    profit_max_heap = []

    # Add all projects to capital min-heap.
    for i in range(len(capitals)):
        heappush(capital_min_heap, (capitals[i], profits[i]))

    # Loop while more projects can be invested in:
    while num_projects > 0:  # k iterations.
        # Move projects from the capital min-heap to the profit max-heap while you have enough
        # capital to invest in them.
        while len(capital_min_heap) > 0 and capital_min_heap[0][0] <= capital:
            project_capital, project_profit = heappop(capital_min_heap)
            heappush(profit_max_heap, (-project_profit, project_capital))

        # We are at a dead end and can't afford to invest in anything.
        if len(profit_max_heap) < 1:
            break

        # Pop a project from the profit max heap and invest in it.
        project_profit, project_capital = heappop(profit_max_heap)  # O(logn)
        capital += (-project_profit)
        num_projects -= 1

    return capital


def test_ex1():
    capitals = [0, 1, 2]
    profits = [1, 2, 3]
    init_capital = 1
    num_projects = 2
    assert maximize_capital(capitals, profits, init_capital, num_projects) == 6


def test_ex2():
    capitals = [0, 1, 2, 3]
    profits = [1, 2, 3, 5]
    init_capital = 0
    num_projects = 3
    assert maximize_capital(capitals, profits, init_capital, num_projects) == 8
