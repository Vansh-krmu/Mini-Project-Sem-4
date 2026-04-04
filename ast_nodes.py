class NumberNode:
    def __init__(self, value):
        self.value = value


class BinaryOpNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class UnaryOpNode:
    def __init__(self, operator, node):
        self.operator = operator
        self.node = node


class VariableNode:
    def __init__(self, name):
        self.name = name


class AssignNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class FunctionNode:
    def __init__(self, func_name, argument):
        self.func_name = func_name
        self.argument = argument
