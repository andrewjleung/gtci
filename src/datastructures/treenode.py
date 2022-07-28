class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    def __eq__(self, other):
        if other is None:
            return False

        return self.val == other.val and self.left == other.left and self.right == other.right
