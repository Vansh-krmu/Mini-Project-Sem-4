import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

from tokenizer import tokenize
from parser import Parser
from evaluator import evaluate, variables


# ---------- Pretty AST ----------
def pretty_tree(node, prefix="", is_left=True):
    if node is None:
        return ""

    result = prefix + ("├── " if is_left else "└── ")

    if hasattr(node, 'value'):
        result += str(node.value) + "\n"
    elif hasattr(node, 'operator'):
        result += node.operator + "\n"
    elif hasattr(node, 'name'):
        result += node.name + "\n"
    elif hasattr(node, 'func_name'):
        result += node.func_name + "\n"

    children = []
    if hasattr(node, 'left'): children.append(node.left)
    if hasattr(node, 'right'): children.append(node.right)
    if hasattr(node, 'node'): children.append(node.node)
    if hasattr(node, 'argument'): children.append(node.argument)

    for i, child in enumerate(children):
        result += pretty_tree(child, prefix + ("│   " if is_left else "    "), i == 0)

    return result
# ---------- GUI ----------
class MiniMathApp:
    def _init_(self, root):
        self.root = root
        self.root.title("ExpressionLab")
        self.root.geometry("900x600")
        root.configure(bg="#1e1e1e")

        # Title
        tk.Label(root, text="ExpressionLab", fg="white", bg="#1e1e1e",
                 font=("Segoe UI", 18, "bold")).pack(pady=10)

        # Input
        self.entry = tk.Entry(root, font=("Segoe UI", 14), width=40)
        self.entry.pack(pady=10)

        # ENTER shortcut
        self.entry.bind("<Return>", lambda event: self.calculate())

        # Buttons
        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Evaluate", command=self.calculate,
                  bg="#007acc", fg="white", font=("Segoe UI", 12)).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="Plot Graph", command=self.plot_graph,
                  bg="#00a86b", fg="white", font=("Segoe UI", 12)).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="Clear", command=self.clear_all,
                  bg="#cc3300", fg="white", font=("Segoe UI", 12)).pack(side=tk.LEFT, padx=5)
        # Result
        self.result = tk.Label(root, text="", fg="white", bg="#1e1e1e",
                               font=("Segoe UI", 14))
        self.result.pack(pady=10)

        # Panels
        frame = tk.Frame(root, bg="#1e1e1e")
        frame.pack()

        self.tree = tk.Text(frame, width=55, height=20, bg="#252526", fg="white")
        self.tree.pack(side=tk.LEFT, padx=10)

        self.history = tk.Listbox(frame, width=35)
        self.history.pack(side=tk.RIGHT, padx=10)
