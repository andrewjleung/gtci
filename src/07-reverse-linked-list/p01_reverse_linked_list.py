from src.datastructures.node import (node, node_eq_array)

"""
Given the head of a singly linked list, reverse the linked list. Write a function to return the new 
head of the reversed linked list.
"""


def reverse(head):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    current = head
    previous = None

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


def test_ex1():
    head = node([2, 4, 6, 8, 10])
    actual = reverse(head)
    expected = [10, 8, 6, 4, 2]
    assert node_eq_array(actual, expected)
