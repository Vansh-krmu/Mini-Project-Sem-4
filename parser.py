'''
Half Code. Add Term Func. & factor func. later.
'''

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
        return self.expression()

    def expression(self):
        node = self.term()

        while self.current_token() and self.current_token()[0] in ('PLUS', 'MINUS'):
            operator = self.eat(self.current_token()[0])[0]
            right = self.term()
            node = BinaryOpNode(node, operator, right)

        return node
