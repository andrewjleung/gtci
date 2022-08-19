from collections import deque

"""
You are given a 2D matrix containing only 1s (land) and 0s (water).

An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

Two islands are considered the same if and only if they can be translated (not rotated or reflected) to equal each other. 

Write a function to find the number of distinct islands in the given matrix.
"""

DIRECTIONS = {
    "u": (-1, 0),
    "r": (0, 1),
    "d": (1, 0),
    "l": (0, -1)
}


def bfs_destroy_and_get_traversal(matrix, row, col, traversal):
    queue = deque([(row, col)])

    while len(queue) > 0:
        row, col = queue.popleft()
        matrix[row][col] = 0
        for direction, (row_diff, col_diff) in DIRECTIONS.items():
            new_row, new_col = row + row_diff, col + col_diff
            if new_row < 0 or new_row >= len(matrix):
                continue
            if new_col < 0 or new_col >= len(matrix[new_row]):
                continue
            if matrix[new_row][new_col] == 0:
                continue
            traversal.append(direction)
            queue.append((new_row, new_col))


def num_distinct_islands_bfs(matrix):
    """
    `m` is the height of the matrix and `n` is the width of the matrix.
    Time Complexity:  O(m * n)
    Space Complexity: O(m * n)
    """
    traversals = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                traversal = []
                bfs_destroy_and_get_traversal(matrix, row, col, traversal)
                traversal = ''.join(traversal)
                traversals.add(traversal)

    return len(traversals)


def dfs_destroy_and_get_traversal(matrix, row, col, traversal, direction):
    if row < 0 or row >= len(matrix):
        return
    if col < 0 or col >= len(matrix[row]):
        return
    if matrix[row][col] == 0:
        return

    matrix[row][col] = 0
    traversal.append(direction)

    for direction, (row_diff, col_diff) in DIRECTIONS.items():
        dfs_destroy_and_get_traversal(
            matrix, row + row_diff, col + col_diff, traversal, direction)


def num_distinct_islands_dfs(matrix):
    """
    `m` is the height of the matrix and `n` is the width of the matrix.
    Time Complexity:  O(m * n)
    Space Complexity: O(m * n)
    """
    traversals = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                traversal = []
                dfs_destroy_and_get_traversal(
                    matrix, row, col, traversal, "")
                traversal = ''.join(traversal)
                traversals.add(traversal)

    return len(traversals)


def test_bfs1():
    matrix = [
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1],
        [0, 1, 1, 0, 1]
    ]
    actual = num_distinct_islands_bfs(matrix)
    expected = 2
    assert actual == expected


def test_bfs2():
    matrix = [
        [1, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 0]
    ]
    actual = num_distinct_islands_bfs(matrix)
    expected = 2
    assert actual == expected


def test_dfs1():
    matrix = [
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1],
        [0, 1, 1, 0, 1]
    ]
    actual = num_distinct_islands_dfs(matrix)
    expected = 2
    assert actual == expected


def test_dfs2():
    matrix = [
        [1, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 0]
    ]
    actual = num_distinct_islands_dfs(matrix)
    expected = 2
    assert actual == expected
