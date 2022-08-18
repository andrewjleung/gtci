from src.datastructures.node import (node, node_eq_array)
from p01_reverse_linked_list import reverse
from p02_reverse_sub_list import reverse_sub

"""
Given the head of a singly linked list and a number `k`, rotate the linked list to the right by `k`
nodes.
"""


def my_rotate(head, k):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    if head is None or head.next is None or k <= 0:
        return head

    # Get the length of the list.
    length = 0
    current = head
    while current is not None:
        current = current.next
        length += 1

    # If `k > length`, then `k` rotations is the same as doing `k % length` rotations.
    k %= length

    # Reverse the entire list.
    head = reverse(head)

    # Reverse the first `k` elements and the last `length - k` elements separately. This will
    # effectively take the last `k` elements and place them at the start, simulating a rotation.
    head = reverse_sub(head, 1, k)
    head = reverse_sub(head, k + 1, length)

    return head


def rotate(head, k):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    if head is None or head.next is None or k <= 0:
        return head

    # Get the length of the list and the last node. The last node is necessary in order to splice to
    # the first node of the head.
    length = 1
    last_node = head
    while last_node.next is not None:
        last_node = last_node.next
        length += 1

    # If `k > length`, then `k` rotations is the same as doing `k % length` rotations.
    k %= length
    skip_length = length - k
    last_node_of_rotated_list = head

    # Skip until the first node of the rotated portion.
    for i in range(skip_length - 1):
        last_node_of_rotated_list = last_node_of_rotated_list.next

    last_node.next = head
    head = last_node_of_rotated_list.next
    last_node_of_rotated_list.next = None

    return head


def test_ex1():
    head = node([1, 2, 3, 4, 5, 6])
    k = 3
    actual = rotate(head, k)
    expected = [4, 5, 6, 1, 2, 3]
    assert node_eq_array(actual, expected)


def test_ex2():
    head = node([1, 2, 3, 4, 5])
    k = 8
    actual = rotate(head, k)
    expected = [3, 4, 5, 1, 2]
    assert node_eq_array(actual, expected)


def test_ex3():
    head = node([1, 2, 3, 4, 5, 6])
    k = 1
    actual = rotate(head, k)
    expected = [6, 1, 2, 3, 4, 5]
    assert node_eq_array(actual, expected)


def test_ex4():
    head = node([1, 2, 3, 4, 5, 6])
    k = 6
    actual = rotate(head, k)
    expected = [1, 2, 3, 4, 5, 6]
    assert node_eq_array(actual, expected)


def test_ex5():
    head = node([1])
    k = 5
    actual = rotate(head, k)
    expected = head
    assert actual == expected
