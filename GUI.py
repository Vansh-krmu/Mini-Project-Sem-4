import tkinter as tk
from tkinter import messagebox

from tokenizer import tokenize
from parser import Parser
from evaluator import evaluate
from errors import LexerError, ParserError, EvaluationError
from ast_nodes import NumberNode, BinaryOpNode


def ast_to_string(node, indent=""):
    if isinstance(node, NumberNode):
        return indent + str(node.value) + "\n"

    if isinstance(node, BinaryOpNode):
        text = indent + node.operator + "\n"
        text += ast_to_string(node.left, indent + "  ")
        text += ast_to_string(node.right, indent + "  ")
        return text

class MiniMathApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Mini-Math Interpreter")
        self.root.geometry("750x500")

        tk.Label(root, text="Mini-Math Interpreter", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(root, text="Enter Expression:").pack()
        self.entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.entry.pack(pady=5)

        tk.Button(root, text="Evaluate", command=self.calculate).pack(pady=10)

        self.result_label = tk.Label(root, text="Result:", font=("Arial", 12))
        self.result_label.pack()

        frame = tk.Frame(root)
        frame.pack(pady=10)
