import tkinter as tk
from tkinter import messagebox
import sys
import os

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
    def __init__(self, root):
        self.root = root
        self.root.title("ExpressionLab")
        self.root.geometry("750x500")

        # Fix icon path for PyInstaller
        if getattr(sys, "frozen", False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        icon_path = os.path.join(base_path, "icon.ico")
        try:
            self.root.iconbitmap(icon_path)
        except:
            pass

        # Title
        tk.Label(root, text="ExpressionLab", font=("Arial", 16, "bold")).pack(pady=10)

        # Input
        tk.Label(root, text="Enter Expression:").pack()
        self.entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.entry.pack(pady=5)

        tk.Button(root, text="Evaluate", command=self.calculate).pack(pady=10)

        # Result
        self.result_label = tk.Label(root, text="Result:", font=("Arial", 12))
        self.result_label.pack()

        # Frame for AST + History
        frame = tk.Frame(root)
        frame.pack(pady=10)

        # AST Panel
        ast_frame = tk.Frame(frame)
        ast_frame.pack(side=tk.LEFT, padx=10)

        tk.Label(ast_frame, text="Abstract Syntax Tree").pack()
        self.ast_text = tk.Text(ast_frame, height=15, width=35)
        self.ast_text.pack()

        # History Panel
        history_frame = tk.Frame(frame)
        history_frame.pack(side=tk.RIGHT, padx=10)

        tk.Label(history_frame, text="Calculation History").pack()
        self.history_list = tk.Listbox(history_frame, height=15, width=30)
        self.history_list.pack()

    def calculate(self):
        expr = self.entry.get()

        try:
            tokens = tokenize(expr)
            parser = Parser(tokens)
            ast = parser.parse()
            result = evaluate(ast)

            # Show result
            self.result_label.config(text=f"Result: {result}")

            # Show AST
            self.ast_text.delete("1.0", tk.END)
            self.ast_text.insert(tk.END, ast_to_string(ast))

            # Add to history
            self.history_list.insert(tk.END, f"{expr} = {result}")

        except (LexerError, ParserError, EvaluationError) as e:
            messagebox.showerror("Error", str(e))
