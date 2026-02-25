from ast_nodes import NumberNode, BinaryOpNode
from errors import ParserError

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, token_type):
        token = self.current_token()
        if token and token[0] == token_type:
            self.pos += 1
            return token
        raise ParserError(f"Expected {token_type}")

    def parse(self):
        node = self.expression()

        if self.current_token() is not None:
            raise ParserError("Unexpected token")

        return node

    def expression(self):
        node = self.term()

        while self.current_token() and self.current_token()[0] in ('PLUS', 'MINUS'):
            operator = self.eat(self.current_token()[0])[0]
            right = self.term()
            node = BinaryOpNode(node, operator, right)

        return node

    def term(self):
        node = self.factor()

        while self.current_token() and self.current_token()[0] in ('MULTIPLY', 'DIVIDE'):
            operator = self.eat(self.current_token()[0])[0]
            right = self.factor()
            node = BinaryOpNode(node, operator, right)

        return node

    def factor(self):
        token = self.current_token()

        if token is None:
            raise ParserError("Unexpected end of input")

        if token[0] == 'NUMBER':
            self.eat('NUMBER')
            return NumberNode(token[1])

        if token[0] == 'LPAREN':
            self.eat('LPAREN')
            node = self.expression()
            self.eat('RPAREN')
            return node

        raise ParserError("Invalid syntax")
