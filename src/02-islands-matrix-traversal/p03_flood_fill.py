from src.testutils import contains_same_elements
from collections import deque

"""
Any image can be represented by a 2D integer array (i.e., a matrix) where each
cell represents the pixel value of the image.

Flood fill algorithm takes a starting cell (i.e., a pixel) and a color. The 
given color is applied to all horizontally and vertically connected cells with
the same color as that of the starting cell. Recursively, the algorithm fills 
cells with the new color until it encounters a cell with a different color than
the starting.
"""

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs_color(matrix, start, color):
    starting_color = matrix[start[0]][start[1]]
    queue = deque([start])

    while len(queue) > 0:
        row, col = queue.popleft()
        matrix[row][col] = color

        for row_diff, col_diff in DIRECTIONS:
            new_row, new_col = row + row_diff, col + col_diff
            if new_row < 0 or new_row >= len(matrix):
                continue
            if new_col < 0 or new_col >= len(matrix[new_row]):
                continue
            if matrix[new_row][new_col] != starting_color:
                continue
            queue.append((new_row, new_col))


def dfs_color(matrix, start, starting_color, fill_color):
    row, col = start
    if row < 0 or row >= len(matrix):
        return
    if col < 0 or col >= len(matrix[row]):
        return
    if matrix[row][col] != starting_color:
        return

    matrix[row][col] = fill_color

    for row_diff, col_diff in DIRECTIONS:
        new_row, new_col = row + row_diff, col + col_diff
        dfs_color(matrix, (new_row, new_col), starting_color, fill_color)


def flood_fill_bfs(matrix, start, color):
    """
    Time Complexity:  O(m * n)
    Space Complexity: O(m * n)
    """
    row, col = start

    if row < 0 or row >= len(matrix):
        return
    if col < 0 or col >= len(matrix[row]):
        return

    bfs_color(matrix, start, color)


def flood_fill_dfs(matrix, start, color):
    row, col = start

    if row < 0 or row >= len(matrix):
        return
    if col < 0 or col >= len(matrix[row]):
        return

    starting_color = matrix[row][col]
    dfs_color(matrix, start, starting_color, color)


def test_bfs1():
    matrix = [
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    starting_cell = (1, 3)
    color = 2
    flood_fill_bfs(matrix, starting_cell, color)
    expected = [
        [0, 2, 2, 2, 0],
        [0, 0, 0, 2, 2],
        [0, 2, 2, 2, 0],
        [0, 2, 2, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert contains_same_elements(matrix, expected)


def test_bfs2():
    matrix = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    starting_cell = (3, 2)
    color = 5
    flood_fill_bfs(matrix, starting_cell, color)
    expected = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 5, 5, 0],
        [0, 0, 5, 0, 0],
        [0, 0, 5, 0, 0]
    ]
    assert contains_same_elements(matrix, expected)


def test_dfs1():
    matrix = [
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    starting_cell = (1, 3)
    color = 2
    flood_fill_dfs(matrix, starting_cell, color)
    expected = [
        [0, 2, 2, 2, 0],
        [0, 0, 0, 2, 2],
        [0, 2, 2, 2, 0],
        [0, 2, 2, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert contains_same_elements(matrix, expected)


def test_dfs2():
    matrix = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    starting_cell = (3, 2)
    color = 5
    flood_fill_dfs(matrix, starting_cell, color)
    expected = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 5, 5, 0],
        [0, 0, 5, 0, 0],
        [0, 0, 5, 0, 0]
    ]
    assert contains_same_elements(matrix, expected)
