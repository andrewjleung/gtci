"""
Given a binary matrix representing an image, we want to flip the image 
horizontally, then invert it.

To flip an image horizontally means that each row of the image is reversed. For
example, flipping [0, 1,1] horizontally results in [1, 1, 0].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by
0. For example, inverting [1, 1, 0] results in [0, 0, 1].
"""


def flip_and_invert(image):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    for row in image:
        l = len(row)
        # Reverse the row while inverting each bit.
        for i in range((l + 1) // 2):
            # Swap both numbers and invert them.
            row[i], row[l - i - 1] = row[l - i - 1] ^ 1, row[i] ^ 1

    return image


def test_ex1():
    image = [
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ]
    actual = flip_and_invert(image)
    expected = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert actual == expected


def test_ex2():
    image = [
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 0, 1, 0]
    ]
    actual = flip_and_invert(image)
    expected = [
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 1, 0]
    ]
    assert actual == expected
