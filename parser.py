from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self):
        self.pos += 1

    def parse(self):
        return self.expr()

    # + -
    def expr(self):
        node = self.term()

        while self.current() and self.current()[1] in ('+', '-'):
            op = self.current()[1]
            self.eat()
            node = BinaryOpNode(node, op, self.term())

        return node

    # * /
    def term(self):
        node = self.power()

        while self.current() and self.current()[1] in ('*', '/'):
            op = self.current()[1]
            self.eat()
            node = BinaryOpNode(node, op, self.power())

        return node

    # ^ (RIGHT ASSOCIATIVE)
    def power(self):
        node = self.factor()

        if self.current() and self.current()[1] == '^':
            op = self.current()[1]
            self.eat()
            node = BinaryOpNode(node, op, self.power())

        return node

    def factor(self):
        token = self.current()

        if token is None:
            return None

        if token[1] == '-':
            self.eat()
            return UnaryOpNode('-', self.factor())

        if token[0] == "NUMBER":
            self.eat()
            return NumberNode(float(token[1]))

        if token[0] == "IDENT":
            name = token[1]
            self.eat()

            if self.current() and self.current()[1] == '=':
                self.eat()
                return AssignNode(name, self.expr())

            return VariableNode(name)

        if token[1] == '(':
            self.eat()
            node = self.expr()
            self.eat()  # )
            return node

        raise Exception("Invalid syntax")
