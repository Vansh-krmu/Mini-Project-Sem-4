import re

TOKEN_SPECIFICATION = [
    ('NUMBER',   r'\d+'),        
    ('PLUS',     r'\+'),         
    ('MINUS',    r'-'),          
    ('MUL',      r'\*'),         
    ('DIV',      r'/'),          
    ('LPAREN',   r'\('),         
    ('RPAREN',   r'\)'),         
    ('SKIP',     r'[ \t]+'),     
    ('MISMATCH', r'.'),          
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)

def tokenize(expression):
    tokens = []

    for match in re.finditer(token_regex, expression):
        kind = match.lastgroup
        value = match.group()

        if kind == 'NUMBER':
            tokens.append(('NUMBER', int(value)))
        elif kind in ('PLUS', 'MINUS', 'MUL', 'DIV', 'LPAREN', 'RPAREN'):
            tokens.append((kind, value))
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f"Invalid character: {value}")

    return tokens
expr = "3 + 4 * (2 - 1) + 78 / 2 (56 * 67)"
print(tokenize(expr))
