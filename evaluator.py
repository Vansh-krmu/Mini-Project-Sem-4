import math
from ast_nodes import *

variables = {}

def evaluate(node):
    if isinstance(node, NumberNode):
        return node.value

    if isinstance(node, UnaryOpNode):
        return -evaluate(node.node)

    if isinstance(node, BinaryOpNode):
        if node.operator == '+':
            return evaluate(node.left) + evaluate(node.right)
        if node.operator == '-':
            return evaluate(node.left) - evaluate(node.right)
        if node.operator == '*':
            return evaluate(node.left) * evaluate(node.right)
        if node.operator == '/':
            return evaluate(node.left) / evaluate(node.right)

    if isinstance(node, VariableNode):
        if node.name in variables:
            return variables[node.name]
        raise Exception(f"Undefined variable {node.name}")

    if isinstance(node, AssignNode):
        value = evaluate(node.value)
        variables[node.name] = value
        return value

    if isinstance(node, FunctionNode):
        val = evaluate(node.argument)
        if node.func_name == "sin":
            return math.sin(val)
        if node.func_name == "cos":
            return math.cos(val)
        if node.func_name == "tan":
            return math.tan(val)

    raise Exception("Evaluation error")
