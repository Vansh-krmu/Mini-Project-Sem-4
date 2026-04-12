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
# ---------- GUI ----------
class MiniMathApp:
    def _init_(self, root):
        self.root = root
        self.root.title("ExpressionLab")
        self.root.geometry("900x600")
        root.configure(bg="#1e1e1e")


        self.db = Database()
        self.evaluator = Evaluator(self.db)

        # Title
        tk.Label(root, text="ExpressionLab", fg="white", bg="#1e1e1e",
                 font=("Segoe UI", 18, "bold")).pack(pady=10)

        # Input
        self.entry = tk.Entry(root, font=("Segoe UI", 14), width=40)
        self.entry.pack(pady=10)
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


        self.load_history()
        
    # ---------- Evaluate ----------
    def calculate(self):
        expr = self.entry.get()

        try:
            tokens = tokenize(expr)
            ast = Parser(tokens).parse()

            result = self.evaluator.evaluate(ast)

            # SAVE TO DB
            self.db.save_history(expr, result)

            self.result.config(text=f"Result: {result}")

            self.tree.delete("1.0", tk.END)
            self.tree.insert(tk.END, pretty_tree(ast))

            self.history.insert(tk.END, f"{expr} = {result}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------- Load History ----------
    def load_history(self):
        try:
            records = self.db.get_history()
            for item in records:
                self.history.insert(tk.END, f"{item['expression']} = {item['result']}")
        except:
            pass

    # ---------- Clear ----------
    def clear_all(self):
        self.entry.delete(0, tk.END)
        self.result.config(text="")
        self.tree.delete("1.0", tk.END)
        self.history.delete(0, tk.END)
 # ---------- Graph ----------
    def plot_graph(self):
        try:
            import numpy as np
            import matplotlib.pyplot as plt

            expr = self.entry.get()

            x_vals = np.linspace(-10, 10, 200)
            y_vals = []

            for x in x_vals:
              
                self.db.save_variable("x", float(x))

                tokens = tokenize(expr)
                ast = Parser(tokens).parse()
                y = self.evaluator.evaluate(ast)

                y_vals.append(y)

            plt.figure()
            plt.plot(x_vals, y_vals)
            plt.title(f"Graph of {expr}")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.grid()
            plt.show()

        except Exception as e:
            messagebox.showerror("Graph Error", str(e))
