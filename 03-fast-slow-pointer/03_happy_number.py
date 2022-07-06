"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal to
the sum of the square of all of its digits, leads us to number `1`. All other (not-happy) numbers
will never reach `1`. Instead, they will be stuck in a cycle of numbers which does not include `1`.
"""


def is_happy_number(n):
    slow = n
    fast = n

    while True:
        slow = next_happy_number(slow)
        fast = next_happy_number(next_happy_number(fast))

        if slow == fast:
            break

    return slow == 1


def next_happy_number(n):
    sum = 0

    while n != 0:
        digit = n % 10
        sum += (digit * digit)
        n = int(n / 10)

    return sum


def test_next_happy_number1():
    assert next_happy_number(23) == 13


def test_next_happy_number2():
    assert next_happy_number(12) == 5


def test_happy_number():
    n = 23
    assert is_happy_number(n)


def test_not_happy_number():
    n = 12
    assert not is_happy_number(n)
