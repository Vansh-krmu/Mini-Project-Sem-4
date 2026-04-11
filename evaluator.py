from ast_nodes import *
from errors import EvaluationError
import math


class Evaluator:
    def __init__(self, db):
        self.db = db

    def evaluate(self, node):

        if isinstance(node, NumberNode):
            return node.value

        elif isinstance(node, UnaryOpNode):
            val = self.evaluate(node.node)

            if node.operator == '-':
                return -val

        elif isinstance(node, BinaryOpNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)

            if node.operator == '+':
                return left + right

            elif node.operator == '-':
                return left - right

            elif node.operator == '*':
                return left * right

            elif node.operator == '/':
                if right == 0:
                    raise EvaluationError("Division by zero")
                return left / right

            elif node.operator == '^':
                return left ** right

        elif isinstance(node, AssignNode):
            value = self.evaluate(node.value)
            self.db.save_variable(node.name, value)
            return value

        elif isinstance(node, VariableNode):
            value = self.db.get_variable(node.name)

            if value is None:
                raise EvaluationError(
                    f"Variable '{node.name}' not defined"
                )

            return value

        elif isinstance(node, FunctionNode):
            val = self.evaluate(node.argument)

            if node.func_name == "sin":
                return math.sin(math.radians(val))

            elif node.func_name == "cos":
                return math.cos(math.radians(val))

            elif node.func_name == "tan":
                return math.tan(math.radians(val))

            elif node.func_name == "sqrt":
                if val < 0:
                    raise EvaluationError("Invalid sqrt")
                return math.sqrt(val)

            elif node.func_name == "log":
                if val <= 0:
                    raise EvaluationError("Invalid log")
                return math.log10(val)

            raise EvaluationError(
                f"Unknown function '{node.func_name}'"
            )

        raise EvaluationError("Invalid expression")
