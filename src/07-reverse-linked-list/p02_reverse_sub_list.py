from src.datastructures.node import node, node_eq_array

"""
Given the head of a linked list and two positions `p` and `q`, reverse the linked list from position
`p` to `q`.
"""


def reverse_sub(head, p, q):
    """
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    if q <= p:
        return head

    i = 1
    current = head
    previous = None
    rev_start = None

    # Skip until `p`.
    while current is not None and i < p:
        previous = current
        current = current.next
        i += 1

    # Keep track of the element before reversal and the first element of the reversal (which will
    # end up being the last one after reversal) in order to splice the reversed section back to the
    # portions of the list before and after it.
    last_node_of_first_part = previous
    last_node_of_sub_list = current

    # Reverse until `q`.
    while current is not None and i <= q:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1

    # This means that p > 1, since `previous` was updated in the first loop.
    # Splice it's next to the last reversed node.
    if last_node_of_first_part is not None:
        last_node_of_first_part.next = previous
    # This means that p == 1, since `previous` wasn't updated in the first loop, staying as `None`.
    # The head is now the last reversed `Node`.
    else:
        head = previous

    # Splice the last node of the reversed sublist to the first node outside of the sublist.
    last_node_of_sub_list.next = current

    return head


def test_ex():
    head = node([1, 2, 3, 4, 5])
    actual = reverse_sub(head, 2, 4)
    expected = [1, 4, 3, 2, 5]
    assert node_eq_array(actual, expected)
