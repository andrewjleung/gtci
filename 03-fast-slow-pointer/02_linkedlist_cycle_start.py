from node import Node

"""
Given the head of a singly linked list that contains a cycle, write a function to find the starting
node of the cycle
"""


def cycle_start(head):
    """
    Time Complexity:  O(N)
    Space Complexity: O(1)
    """
    slow = head
    fast = head

    # Move the pointers to the same point within the cycle.
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            length = 1
            fast = fast.next

            # Get the length of the cycle.
            while slow != fast:
                length += 1
                fast = fast.next

            slow = head
            fast = head

            # Increment one pointer by the cycle length.
            for i in range(length):
                fast = fast.next

            # Iterate until the two pointers meet again at the cycle start.
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow

    return None


def test_cycle1():
    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    head.next.next.next.next.next.next = head.next.next

    assert cycle_start(head).value == 3


def test_cycle2():
    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    head.next.next.next.next.next.next = head.next.next.next

    assert cycle_start(head).value == 4


def test_cycle3():
    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    head.next.next.next.next.next.next = head

    assert cycle_start(head).value == 1


def test_no_cycle():
    head = Node(2, Node(4, Node(6, Node(8, Node(10)))))

    assert cycle_start(head) is None
