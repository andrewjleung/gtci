import math
from collections import deque

"""
Given a 2D array (i.e. a matrix) containing only 1s (land) and 0s (water), find 
the biggest island in it. Write a function to return the area of the biggest 
island.

An island is a connected set of 1s (land) and is surrounded by either an edge or
0s (water). Each cell is considered connected to other cells horizontally or 
vertically (not diagonally).
"""

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs_destroy_and_measure(matrix, row, col):
    queue = deque([(row, col)])
    size = 0

    while len(queue) > 0:
        row, col = queue.popleft()
        matrix[row][col] = 0
        size += 1

        for row_diff, col_diff in DIRECTIONS:
            new_row = row + row_diff
            new_col = col + col_diff

            if new_row < 0 or new_row >= len(matrix):
                continue
            if new_col < 0 or new_col >= len(matrix[new_row]):
                continue
            if matrix[new_row][new_col] == 0:
                continue
            queue.append((new_row, new_col))

    return size


def dfs_destroy_and_measure(matrix, row, col):
    if row < 0 or row >= len(matrix):
        return 0
    if col < 0 or col >= len(matrix[row]):
        return 0
    if matrix[row][col] == 0:
        return 0

    matrix[row][col] = 0
    size = 1
    for row_diff, col_diff in DIRECTIONS:
        size += dfs_destroy_and_measure(matrix, row + row_diff, col + col_diff)
    return size


def biggest_island(matrix, destroy_and_measure=bfs_destroy_and_measure):
    """
    `m` is the height of the matrix, `n` is the width of the matrix.
    Time Complexity:  O(m * n)
    Space Complexity: O(m * n)
    """
    biggest_island = -math.inf

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                island_size = destroy_and_measure(matrix, row, col)
                biggest_island = max(biggest_island, island_size)

    return biggest_island


def test_bfs1():
    matrix = [
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    actual = biggest_island(matrix)
    expected = 5
    assert actual == expected


def test_dfs1():
    matrix = [
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    actual = biggest_island(matrix, dfs_destroy_and_measure)
    expected = 5
    assert actual == expected
