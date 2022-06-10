"""
Given two strings containing backspaces (#), check if the two strings are equal
"""


def compare_strings_w_backspaces(str1, str2):
    """
    Time Complexity:  O(n + m)
    Space Complexity: O(1)
    """
    str1_ptr = len(str1) - 1
    str2_ptr = len(str2) - 1
    str1_skips, str2_skips = 0, 0

    while str1_ptr >= 0 or str2_ptr >= 0:
        if str1[str1_ptr] == "#":
            str1_skips += 1
            str1_ptr -= 1

        if str2[str2_ptr] == "#":
            str2_skips += 1
            str2_ptr -= 1

        while str1_skips > 0:
            if str1[str1_ptr] != "#":
                str1_skips -= 1
            else:
                str1_skips += 1
            str1_ptr -= 1

        while str2_skips > 0:
            if str2[str2_ptr] != "#":
                str2_skips -= 1
            else:
                str2_skips += 1
            str2_ptr -= 1

        if str1[str1_ptr] != str2[str2_ptr]:
            return False

        if (str1_ptr == 0 or str2_ptr == 0) and str1_ptr != str2_ptr:
            return False

        str1_ptr -= 1
        str2_ptr -= 1

    return True


def test_ex1():
    str1 = "xy#z"
    str2 = "xzz#"
    o = True
    assert compare_strings_w_backspaces(str1, str2) == o


def test_ex2():
    str1 = "xy#z"
    str2 = "xyz#"
    o = False
    assert compare_strings_w_backspaces(str1, str2) == o


def test_ex3():
    str1 = "xp#"
    str2 = "xyz##"
    o = True
    assert compare_strings_w_backspaces(str1, str2) == o


def test_ex4():
    str1 = "xywrrmp"
    str2 = "xywrrmu#p"
    o = True
    assert compare_strings_w_backspaces(str1, str2) == o
