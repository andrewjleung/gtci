class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def structeq(self, other):
        if other is None:
            return False

        return self.value == other.value and ((self.next is None and other.next is None) or (self.next.structeq(other.next)))


def node_eq_array(head, arr):
    for i in range(len(arr)):
        if head is None or head.value != arr[i]:
            return False

        head = head.next

    return head is None


def test_node_eq_array_empty():
    head = node([])
    assert node_eq_array(head, [])


def test_node_eq_array_diff_len1():
    head = node([1, 2, 3])
    assert not node_eq_array(head, [1, 2])


def test_node_eq_array_diff_len2():
    head = node([1, 2])
    assert not node_eq_array(head, [1, 2, 3])


def test_node_eq_array_diff_not_eq1():
    head = node([1, 2, 4])
    assert not node_eq_array(head, [1, 2, 3])


def test_node_eq_array_diff_not_eq2():
    head = node([0, 2, 4])
    assert not node_eq_array(head, [1, 2, 3])


def node(lst):
    if len(lst) < 1:
        return None

    return Node(lst[0], node(lst[1:]))


def test_empty():
    assert node([]) == None


def test_nonempty1():
    assert node([1]).structeq(Node(1))


def test_nonempty2():
    assert node([1, 2, 3, 4]).structeq(Node(1, Node(2, Node(3, Node(4)))))
