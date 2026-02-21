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
