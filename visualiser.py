from ast_nodes import NumberNode, BinaryOpNode

def print_ast(node, indent=""):
    if isinstance(node, NumberNode):
        print(indent + str(node.value))
    elif isinstance(node, BinaryOpNode):
        print(indent + node.operator)
        print_ast(node.left, indent + "  ")
        print_ast(node.right, indent + "  ")
