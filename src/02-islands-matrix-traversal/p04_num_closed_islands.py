from collections import deque

"""
You are given a 2D matrix containing only 1s (land) and 0s (water).

An island is a connected set of 1s (land) and is surrounded by either an edge or
0s (water). Each cell is considered connected to other cells horizontally or 
vertically (not diagonally).

A closed island is an island that is totally surrounded by 0s (i.e., water). 
This means all horizontally and vertically connected cells of a closed island 
are water. This also means that, by definition, a closed island can't touch an 
edge (as then the edge cells are not connected to any water cell).

Write a function to find the number of closed islands in the given matrix.
"""

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs_destroy_and_is_closed(matrix, row, col):
    queue = deque([(row, col)])
    is_closed = True

    while len(queue) > 0:
        row, col = queue.popleft()
        matrix[row][col] = 0

        for row_diff, col_diff in DIRECTIONS:
            new_row, new_col = row + row_diff, col + col_diff
            if new_row < 0 or new_row >= len(matrix):
                is_closed = False
                continue
            if new_col < 0 or new_col >= len(matrix[new_row]):
                is_closed = False
                continue
            if matrix[new_row][new_col] == 0:
                continue
            queue.append((new_row, new_col))

    return is_closed


def num_closed_islands_bfs(matrix):
    """
    `m` is the height of the matrix, `n` is the width of the matrix.
    Time Complexity:  O(m * n)
    Space Complexity: O(m * n)
    """
    count = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                if bfs_destroy_and_is_closed(matrix, row, col):
                    count += 1

    return count


def dfs_destroy_and_is_closed(matrix, row, col):
    if row < 0 or row >= len(matrix):
        return False
    if col < 0 or col >= len(matrix[row]):
        return False
    if matrix[row][col] == 0:
        return True

    matrix[row][col] = 0
    is_closed = True

    for row_diff, col_diff in DIRECTIONS:
        is_closed &= dfs_destroy_and_is_closed(
            matrix, row + row_diff, col + col_diff)

    return is_closed


def num_closed_islands_dfs(matrix):
    count = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                if dfs_destroy_and_is_closed(matrix, row, col):
                    count += 1

    return count


def test_bfs1():
    matrix = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    actual = num_closed_islands_bfs(matrix)
    expected = 1
    assert actual == expected


def test_bfs2():
    matrix = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    actual = num_closed_islands_bfs(matrix)
    expected = 2
    assert actual == expected


def test_dfs1():
    matrix = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    actual = num_closed_islands_dfs(matrix)
    expected = 1
    assert actual == expected


def test_dfs2():
    matrix = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    actual = num_closed_islands_dfs(matrix)
    expected = 2
    assert actual == expected
