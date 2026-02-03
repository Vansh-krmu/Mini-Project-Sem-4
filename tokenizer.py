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
