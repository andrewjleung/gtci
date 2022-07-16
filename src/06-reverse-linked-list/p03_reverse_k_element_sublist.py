from src.datastructures.node import (node, node_eq_array)

"""
Given the head of a linked list and a number `k`, reverse every `k` sized sub-list starting from the
head.

If, in the end, you are left with a sub-list with less than `k` elements, reverse it too.
"""


def reverse_k(head, k):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    if k < 1 or head is None:
        return head

    previous = None
    current = head

    while True:
        # The last of the previous sub-list is needed in order to connect the previous sub-list to
        # the current sub-list after it has been reversed.
        last_of_previous_sublist = previous
        last_of_current_sublist = current

        # Reverse `k` nodes.
        i = 0
        while current is not None and i < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        if last_of_previous_sublist is not None:
            # After reversing this sub-list, previous will now contain the new first element of this
            # sub-list, which can be set as the `next` of the previous sub-list's last item.
            last_of_previous_sublist.next = previous
        else:
            # `last_of_previous_sublist` is only `None` for the first sub-list. Since `head` is what
            # we are ultimately returning, we want it to be the last element of the original first
            # sub-list, which `previous` contains after reversing.
            head = previous

        # Connect the current reversed sub-list to the head of the next un-reversed sub-list.
        # At this current point, the last of the current sub-list is pointing to its previous which
        # is the last of the previous sub-list. However due to the previous if-statement, the last
        # of the previous sub-list is now pointing to the first of the current sub-list, forming a
        # cycle. To break the cycle, we need to point the last of the current sub-list to the next
        # sub-list.
        #
        # Consider the loop invariant being that the current list is as if all sub-lists up to now
        # are reversed, while all after are un-reversed.
        last_of_current_sublist.next = current

        if current is None:
            break

        # `previous` currently contains the last element of the original current sub-list, while we
        # need it to contain the last element of the reversed current sub-list, which
        # `last_of_current_sublist` contains. This needs to be retained for the next sub-list's
        # reversal in order to be able to connect that sub-list with this sub-list.
        previous = last_of_current_sublist

    return head


def test_ex1():
    head = node([1, 2, 3, 4, 5, 6, 7, 8])
    k = 3
    actual = reverse_k(head, k)
    expected = [3, 2, 1, 6, 5, 4, 8, 7]
    actual.print_list()
    assert node_eq_array(actual, expected)


def test_ex2():
    head = node([1, 2, 3, 4, 5, 6])
    k = 3
    actual = reverse_k(head, k)
    expected = [3, 2, 1, 6, 5, 4]
    actual.print_list()
    assert node_eq_array(actual, expected)


def test_ex3():
    head = None
    k = 3
    actual = reverse_k(head, k)
    assert actual is None


def test_ex4():
    head = node([1, 2, 3])
    k = 2
    actual = reverse_k(head, k)
    expected = [2, 1, 3]
    actual.print_list()
    assert node_eq_array(actual, expected)


def test_ex5():
    head = node([1, 2, 3])
    k = 1
    actual = reverse_k(head, k)
    expected = [1, 2, 3]
    actual.print_list()
    assert node_eq_array(actual, expected)


def test_ex6():
    head = node([1, 2, 3])
    k = 4
    actual = reverse_k(head, k)
    expected = [3, 2, 1]
    actual.print_list()
    assert node_eq_array(actual, expected)
