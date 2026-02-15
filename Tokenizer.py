import re

# Token specification
TOKEN_SPECIFICATION = [
    ('NUMBER',   r'\d+'),        # Integer number
    ('PLUS',     r'\+'),         # Addition
    ('MINUS',    r'-'),          # Subtraction
    ('MUL',      r'\*'),         # Multiplication
    ('DIV',      r'/'),          # Division
    ('LPAREN',   r'\('),         # Left Parenthesis
    ('RPAREN',   r'\)'),         # Right Parenthesis
    ('SKIP',     r'[ \t]+'),     # Skip spaces and tabs
    ('MISMATCH', r'.'),          # Any other character
]

# Combine all token patterns into one regex
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
