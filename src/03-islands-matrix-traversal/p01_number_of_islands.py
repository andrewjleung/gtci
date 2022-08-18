from collections import deque

"""
Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water),
count the number of islands in it.

An island is a connected set of 1s (land) and is surrounded by either an edge or
0s (water). Each cell is considered connected to other cells horizontally or
vertically.
"""

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(matrix, row, col):
    queue = deque()
    queue.append((row, col))

    while len(queue) > 0:
        r, c = queue.popleft()
        matrix[r][c] = 0
        for r_diff, c_diff in DIRECTIONS:
            new_r = r + r_diff
            new_c = c + c_diff
            if new_r < 0 or new_r >= len(matrix):
                continue
            if new_c < 0 or new_c >= len(matrix[new_r]):
                continue
            if matrix[new_r][new_c] == 0:
                continue
            queue.append((new_r, new_c))


def dfs(matrix, row, col):
    if row < 0 or row >= len(matrix):
        return
    if col < 0 or col >= len(matrix[row]):
        return
    if matrix[row][col] == 0:
        return

    matrix[row][col] = 0

    for r_diff, c_diff in DIRECTIONS:
        dfs(matrix, row + r_diff, col + c_diff)


def num_islands(matrix, traverse=bfs):
    """
    `m` is the number of rows, `n` is the number of columns.
    Time Complexity:  O(m * n)
    Space Complexity: O(m * n)
        - Regardless of BFS or DFS, if the island is all 1s, in the worst case
          you need space for every single cell either for the BFS queue or the
          DFS recursive call stack.
    """
    count = 0

    # Iterate through every single cell. When reaching an island, count it and
    # search the entire island to zero it out (wipe it off the map). This way
    # you can't possibly double count it.
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                count += 1
                traverse(matrix, row, col)

    return count


def test_bfs1():
    matrix = [
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    actual = num_islands(matrix)
    expected = 1
    assert actual == expected


def test_bfs2():
    matrix = [
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    actual = num_islands(matrix)
    expected = 3
    assert actual == expected


def test_dfs1():
    matrix = [
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    actual = num_islands(matrix, dfs)
    expected = 1
    assert actual == expected


def test_dfs2():
    matrix = [
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    actual = num_islands(matrix, dfs)
    expected = 3
    assert actual == expected
