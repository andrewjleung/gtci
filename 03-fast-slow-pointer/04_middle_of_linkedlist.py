from node import Node

"""
Given the head of a singly linked list, write a method to return the middle node of the linked list.

If the total number of nodes in the linked list is even, return the second middle node.
"""


def get_middle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def test_odd_elements1():
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    o = 3
    assert get_middle(head).value == o


def test_odd_elements2():
    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
    o = 4
    assert get_middle(head).value == o


def test_even_elements():
    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    o = 4
    assert get_middle(head).value == o
