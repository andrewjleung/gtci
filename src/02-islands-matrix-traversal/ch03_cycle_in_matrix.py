"""
You are given a 2D matrix containing different characters, you need to find if there exists any cycle consisting of the same character in the matrix.

A cycle is a path in the matrix that starts and ends at the same cell and has four  or more cells. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same character value of the current cell. 

Write a function to find if the matrix has a cycle.
"""

DIRECTIONS = {
    "u": (-1, 0, "d"),
    "r": (0, 1, "l"),
    "d": (1, 0, "u"),
    "l": (0, -1, "r")
}


def dfs_visit_and_check_cycle(matrix, visited, row, col, char, direction_taken):
    if row < 0 or row >= len(matrix):
        return False
    if col < 0 or col >= len(matrix[row]):
        return False
    if matrix[row][col] != char:
        return False
    if visited[row][col]:
        return True

    visited[row][col] = True
    has_cycle = False

    for direction, (row_diff, col_diff, opposite) in DIRECTIONS.items():
        if direction_taken != opposite:
            has_cycle |= dfs_visit_and_check_cycle(
                matrix, visited, row + row_diff, col + col_diff, char, direction)

    return has_cycle


def cycle_in_matrix(matrix):
    """
    Time Complexity:  O(m * n)
    Space Complexity: O(m * n)
    """
    visited = [[False for _ in range(len(matrix[row]))]
               for row in range(len(matrix))]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not visited[row][col]:
                if dfs_visit_and_check_cycle(matrix, visited, row, col, matrix[row][col], "o"):
                    return True

    return False


def test_ex1():
    matrix = [
        "aaaa",
        "baca",
        "baca",
        "baaa"
    ]
    actual = cycle_in_matrix(matrix)
    expected = True
    assert actual == expected


def test_ex2():
    matrix = [
        "aaaa",
        "abba",
        "abaa",
        "aaac"
    ]
    actual = cycle_in_matrix(matrix)
    expected = True
    assert actual == expected


def test_ex3():
    matrix = [
        "abeb",
        "bbcb",
        "bccd",
        "dcdd"
    ]
    actual = cycle_in_matrix(matrix)
    expected = False
    assert actual == expected
