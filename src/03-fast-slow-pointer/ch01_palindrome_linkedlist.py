from p04_middle_of_linkedlist import get_middle
from src.datastructures.node import Node


"""
Given the head of a singly linked list, write a method to check if the linked list is a palindrome 
or not.

Your algorithm should use constant space and the input linked list should be in the original form
once the algorithm is finished. The algorithm should have O(n) time complexity where `N` is the
number of nodes in the linked list.
"""


def is_palindrome(head):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    # Find the middle of the list.
    middle = get_middle(head)
    head_second_half = reverse(middle)
    copy_head_second_half = head_second_half

    while head is not None and head_second_half is not None:
        if head.value != head_second_half.value:
            break

        head = head.next
        head_second_half = head_second_half.next

    reverse(copy_head_second_half)

    if head is None or head_second_half is None:
        return True

    return False


def reverse(head):
    # Note that this reverses in place.
    prev = None

    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev


def test_is_palindrome1():
    head = Node(2, Node(4, Node(6, Node(4, Node(2)))))
    assert is_palindrome(head)


def test_is_palindrome2():
    head = Node(2, Node(4, Node(6, Node(6, Node(4, Node(2))))))
    assert is_palindrome(head)


def test_is_not_palindrome():
    head = Node(2, Node(4, Node(6, Node(4, Node(2, Node(2))))))
    assert not is_palindrome(head)
