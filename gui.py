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
