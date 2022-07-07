from node import node
from p04_middle_of_linkedlist import get_middle
from ch01_palindrome_linkedlist import reverse

"""
Given the head of a singly linked list, write a method to modify the linked list such that the nodes
from the second half of the linked list are inserted alternately to the nodes from the first half in
reverse order.

Your algorithm should not use any extra space and the input linked list should be modified in place.
"""


def rearrange(head):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    middle = get_middle(head)
    head_second_half = reverse(middle)
    head_first_half = head

    while head_first_half is not None and head_second_half is not None:
        temp = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = temp

        temp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = temp

    if head_first_half is not None:
        head_first_half.next = None


# These do NOT verify that the linked list was modified in place.
def test_ex1():
    head = node([2, 4, 6, 8, 10, 12])
    rearrange(head)
    o = node([2, 12, 4, 10, 6, 8])
    assert head.structeq(o)


def test_ex2():
    head = node([2, 4, 6, 8, 10])
    rearrange(head)
    o = node([2, 10, 4, 8, 6])
    assert head.structeq(o)
