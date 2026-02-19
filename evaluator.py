from ast_nodes import NumberNode, BinaryOpNode
from errors import EvaluationError

def evaluate(node):
    if isinstance(node, NumberNode):
        return node.value

    if isinstance(node, BinaryOpNode):
        left = evaluate(node.left)
        right = evaluate(node.right)

        if node.operator == 'PLUS':
            return left + right
        elif node.operator == 'MINUS':
            return left - right
        elif node.operator == 'MULTIPLY':
            return left * right
        elif node.operator == 'DIVIDE':
            if right == 0:
                raise EvaluationError("Division by zero")
            return left / right

    raise EvaluationError("Invalid AST")
