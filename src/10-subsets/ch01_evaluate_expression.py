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

"""
WITH MEMOIZATION:

Time Complexity:  O(n^2)
    - O(n^2) sub-expressions in an expression
Space Complexity: O(n * cat(n))
    - n eval subarrays, each of size O(cat(n))
"""

OPS = {
    "+": lambda l, r: l + r,
    "-": lambda l, r: l - r,
    "*": lambda l, r: l * r
}


class EvaluateAllExpressions:
    def __init__(self):
        self.memo = {}
        self.hits = 0
        self.calls = 0

    def do_cartesian_op(self, left_evals, op, right_evals):
        evals = []

        for left in left_evals:
            for right in right_evals:
                op_fn = OPS[op]
                evals.append(op_fn(left, right))

        return evals

    def evaluate_all_expressions(self, expr):

        # Use memoization!
        if expr in self.memo:
            self.hits += 1
            return self.memo[expr]

        self.calls += 1
        # Base case. An expression of a single number evaluates to itself.
        if len(expr) == 1:
            return [int(expr)]

        evals = []

        # Iterate through every char looking for operators.
        for i in range(len(expr)):
            # Assuming well-formedness, anything that isn't a number is an operator.
            if not expr[i].isnumeric():
                # Recursively evaluate the left and right expressions relative to this operator.
                left_evals = self.evaluate_all_expressions(expr[:i])
                right_evals = self.evaluate_all_expressions(expr[i + 1:])

                # Calculate the Cartesian product of the left and right evaluations.
                evals += self.do_cartesian_op(left_evals, expr[i], right_evals)

        self.memo[expr] = evals

        return evals


def test_ex1():
    expr = "1+2*3"
    e = EvaluateAllExpressions()
    actual = e.evaluate_all_expressions(expr)
    expected = [7, 9]
    print(f"calls: {e.calls}\nhits:  {e.hits}")
    assert contains_same_elements(actual, expected)


def test_ex2():
    expr = "2*3-4-5"
    e = EvaluateAllExpressions()
    actual = e.evaluate_all_expressions(expr)
    expected = [8, -12, 7, -7, -3]
    print(f"calls: {e.calls}\nhits:  {e.hits}")
    assert contains_same_elements(actual, expected)


def test_ex3():
    expr = "1+1*1"
    e = EvaluateAllExpressions()
    actual = e.evaluate_all_expressions(expr)
    expected = [2, 2]
    print(f"calls: {e.calls}\nhits:  {e.hits}")
    assert contains_same_elements(actual, expected)
