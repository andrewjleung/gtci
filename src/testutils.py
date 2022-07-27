def contains_same_elements(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for arr in arr1:
        if arr not in arr2:
            return False

    return True
