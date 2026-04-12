import tkinter as tk
from tkinter import messagebox

from tokenizer import tokenize
from parser import Parser
from evaluator import Evaluator
from database import Database


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

    children = []
    if hasattr(node, 'left'): children.append(node.left)
    if hasattr(node, 'right'): children.append(node.right)
    if hasattr(node, 'node'): children.append(node.node)

    for i, child in enumerate(children):
        result += pretty_tree(child, prefix + ("│   " if is_left else "    "), i == 0)

    return result
