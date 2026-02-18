class NumberNode:
    def __init__(self, value):
        self.value = value

class BinaryOpNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
