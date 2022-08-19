from collections import deque

"""
You are given a 2D matrix containing only 1s (land) and 0s (water).

An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

There are no lakes on the island, so the water inside the island is not connected to the water around it. A cell is a square with a side length of 1.. 

The given matrix has only one island, write a function to find the perimeter of that island.
"""


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs_destroy_and_count_perimeter(matrix, row, col):
    queue = deque([(row, col)])
    perimeter = 0

    while len(queue) > 0:
        row, col = queue.popleft()
        # Don't zero out the cell. This may get mistaken as an edge further in
        # the traversal. Instead, use a value that you can recognize as neither
        # land or water which can be ignored if re-traversed.
        matrix[row][col] = -1

        for row_diff, col_diff in DIRECTIONS:
            new_row, new_col = row + row_diff, col + col_diff
            if new_row < 0 or new_row >= len(matrix) \
                    or new_col < 0 or new_col >= len(matrix[new_row]) \
                    or matrix[new_row][new_col] == 0:
                perimeter += 1
                continue

            if matrix[new_row][new_col] == -1:
                continue

            queue.append((new_row, new_col))

    return perimeter


def num_closed_islands_bfs(matrix):
    """
    `m` is the height of the matrix, `n` is the width of the matrix.
    Time Complexity:  O(m * n)
    Space Complexity: O(m * n)
    """
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                return bfs_destroy_and_count_perimeter(matrix, row, col)


def dfs_destroy_and_count_perimeter(matrix, row, col):
    if row < 0 or row >= len(matrix) \
            or col < 0 or col >= len(matrix[row]) \
            or matrix[row][col] == 0:
        return 1

    if matrix[row][col] == -1:
        return 0

    matrix[row][col] = -1
    perimeter = 0

    for row_diff, col_diff in DIRECTIONS:
        perimeter += dfs_destroy_and_count_perimeter(
            matrix, row + row_diff, col + col_diff)

    return perimeter


def num_closed_islands_dfs(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                return dfs_destroy_and_count_perimeter(matrix, row, col)


def test_bfs1():
    matrix = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    actual = num_closed_islands_bfs(matrix)
    expected = 14
    assert actual == expected


def test_bfs2():
    matrix = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0]
    ]
    actual = num_closed_islands_bfs(matrix)
    expected = 12
    assert actual == expected


def test_dfs1():
    matrix = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    actual = num_closed_islands_dfs(matrix)
    expected = 14
    assert actual == expected


def test_dfs2():
    matrix = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0]
    ]
    actual = num_closed_islands_dfs(matrix)
    expected = 12
    assert actual == expected
