def contains_same_elements(actual, expected):
    if len(actual) != len(expected):
        return False

    for arr in actual:
        if arr not in expected:
            return False

    return True


def actual_in_expected(actual, expected):
    for el in expected:
        if contains_same_elements(actual, el):
            return True

    return False
