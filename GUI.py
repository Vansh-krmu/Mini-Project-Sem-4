import tkinter as tk
from tkinter import messagebox
from tokenizer import tokenize
from parser import Parser
from evaluator import evaluate
from errors import LexerError, ParserError, EvaluationError
from ast_nodes import NumberNode, BinaryOpNode


# Function to convert AST to string
def ast_to_string(node, indent=""):
    if isinstance(node, NumberNode):
        return indent + str(node.value) + "\n"

    if isinstance(node, BinaryOpNode):
        text = indent + node.operator + "\n"
        text += ast_to_string(node.left, indent + "  ")
        text += ast_to_string(node.right, indent + "  ")
        return text


# Calculate button functionality
def calculate():
    expr = entry.get()

    try:
        tokens = tokenize(expr)
        parser = Parser(tokens)
        ast = parser.parse()

        result = evaluate(ast)

        result_label.config(text=f"Result: {result}")

        ast_text.delete("1.0", tk.END)
        ast_text.insert(tk.END, ast_to_string(ast))

        # Add calculation to history
        history_list.insert(tk.END, f"{expr} = {result}")

    except (LexerError, ParserError, EvaluationError) as e:
        messagebox.showerror("Error", str(e))
