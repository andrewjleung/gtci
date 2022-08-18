from src.datastructures.node import Node


"""
Given the head of a singly linked list, write a function to determine if the linked list has a cycle
in it or not.
"""


def has_cycle(ll):
    """
    Time Complexity:  O(N)
    Space Complexity: O(1)
    """
    slow = ll
    fast = ll

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def test_cycle():
    ll = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    ll.next.next.next.next.next.next = ll.next.next

    assert has_cycle(ll)


def test_no_cycle1():
    ll = Node(2, Node(4, Node(6, Node(8, Node(10)))))

    assert not has_cycle(ll)


def test_no_cycle2():
    ll = Node(2, Node(4, Node(6, Node(8))))

    assert not has_cycle(ll)


def test_no_cycle3():
    ll = None

    assert not has_cycle(ll)
