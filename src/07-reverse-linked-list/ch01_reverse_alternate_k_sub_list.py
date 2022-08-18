from src.datastructures.node import (node, node_eq_array)

"""
Given the head of a linked list and a number `k`, reverse every alternating `k` sized sub-list 
starting from the head.

If, in the end, you are left with a sub-list with less than `k` elements, reverse it too.
"""


def reverse_k_alt(head, k):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    if head is None or k < 2:
        return head

    reversing = True
    previous = None
    current = head

    # Loop through each sub-list.
    while current is not None:
        last_node_of_previous_sublist = previous
        last_node_of_current_sublist = current

        # Reverse `k` nodes.
        i = 0
        while current is not None and i < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        if last_node_of_previous_sublist is not None:
            # The previous sub-list needs to have its last node updated to point to what is now
            # the first node of the current reversed sub-list.
            last_node_of_previous_sublist.next = previous
        else:
            # This is the first sub-list. Head needs to be updated to contain the original last
            # element of this sub-list which is now the first element of the reversed sub-list.
            head = previous

        # The current sub-list needs to point to the start of the next sub-list.
        last_node_of_current_sublist.next = current

        # `previous` currently contains the first element of the reversed sub-list. After
        # reversing, it should hold the last element of the reversed sub-list.
        previous = last_node_of_current_sublist

        # Skip `k` nodes.
        i = 0
        while current is not None and i < k:
            previous = current
            current = current.next
            i += 1

    return head


def test_ex1():
    head = node([1, 2, 3, 4, 5, 6, 7, 8])
    k = 2
    actual = reverse_k_alt(head, k)
    expected = [2, 1, 3, 4, 6, 5, 7, 8]
    assert node_eq_array(actual, expected)


def test_ex2():
    head = node([1, 2, 3, 4, 5, 6, 7, 8])
    k = 3
    actual = reverse_k_alt(head, k)
    expected = [3, 2, 1, 4, 5, 6, 8, 7]
    assert node_eq_array(actual, expected)


def test_ex3():
    head = node([1, 2, 3, 4, 5, 6, 7, 8])
    k = 4
    actual = reverse_k_alt(head, k)
    expected = [4, 3, 2, 1, 5, 6, 7, 8]
    assert node_eq_array(actual, expected)


def test_ex4():
    head = node([1, 2, 3, 4, 5, 6, 7, 8])
    k = 5
    actual = reverse_k_alt(head, k)
    expected = [5, 4, 3, 2, 1, 6, 7, 8]
    assert node_eq_array(actual, expected)


def test_k_1():
    head = node([1, 2, 3, 4, 5, 6, 7, 8])
    k = 1
    actual = reverse_k_alt(head, k)
    expected = head
    assert actual == expected
