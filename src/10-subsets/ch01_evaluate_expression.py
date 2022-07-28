from src.testutils import contains_same_elements


"""
Given an expression containing digits and operations (+, -, *), find all possible ways in which the
expression can be evaluated by grouping the numbers and operators using parentheses.
"""

"""
- Numbers consist of a single digit.
- A non-trivial grouping groups at least a single operator.
- Groupings can be nested.
- There must be at least one grouping.
- Every ordering of execution may only appear once, even if there are different groupings involved.
"""

OPS = {
    "+": lambda l, r: l + r,
    "-": lambda l, r: l - r,
    "*": lambda l, r: l * r
}


def do_cartesian_op(left_evals, op, right_evals):
    evals = []

    for left in left_evals:
        for right in right_evals:
            op_fn = OPS[op]
            evals.append(op_fn(left, right))

    return evals


def evaluate(expr):
    """
    Time Complexity:  O(n * cat(n))
        - A grouped expression is just a binary tree. The number of expressions with distinct 
          groupings that can be created from a given expression is just the number of binary trees 
          with O(n) nodes (each operator is a node, an expression has O(n) operators).
        - The number of binary trees with n nodes is the nth Catalan number.
        - Each expression takes O(n) time to evaluate (copy the string, execute the operations).

    Space Complexity: O(cat(n))
        - Storing the results for `cat(n)` evaluations.
    """
    # Base case. An expression of a single number evaluates to itself.
    if len(expr) == 1:
        return [int(expr)]

    evals = []

    # Iterate through every char looking for operators.
    for i in range(len(expr)):
        # Assuming well-formedness, anything that isn't a number is an operator.
        if not expr[i].isnumeric():
            # Recursively evaluate the left and right expressions relative to this operator.
            left_evals = evaluate(expr[:i])
            right_evals = evaluate(expr[i + 1:])

            # Calculate the Cartesian product of the left and right evaluations.
            evals += do_cartesian_op(left_evals, expr[i], right_evals)

    return evals


def test_ex1():
    expr = "1+2*3"
    actual = evaluate(expr)
    expected = [7, 9]
    assert contains_same_elements(actual, expected)


def test_ex2():
    expr = "2*3-4-5"
    actual = evaluate(expr)
    expected = [8, -12, 7, -7, -3]
    assert contains_same_elements(actual, expected)


def test_ex3():
    expr = "1+1*1"
    actual = evaluate(expr)
    expected = [2, 2]
    assert contains_same_elements(actual, expected)
