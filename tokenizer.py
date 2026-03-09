import re
from errors import LexerError

TOKEN_SPEC = [
    ('NUMBER',   r'\d+(\.\d+)?'),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('MULTIPLY', r'\*'),
    ('DIVIDE',   r'/'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('SKIP',     r'[ \t]+'),
    ('MISMATCH', r'.')
]

def tokenize(code):
    tokens = []
    regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

    for match in re.finditer(regex, code):
        kind = match.lastgroup
        value = match.group()

        if kind == 'NUMBER':
            tokens.append((kind, float(value)))
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise LexerError(f"Invalid character: {value}")
        else:
            tokens.append((kind, value))

    return tokens
