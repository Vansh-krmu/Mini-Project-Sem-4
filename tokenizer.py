import re
from errors import LexerError

TOKEN_SPEC = [
    ("NUMBER", r"\d+(\.\d+)?"),
    ("IDENT", r"[a-zA-Z_]\w*"),
    ("OP", r"[\+\-\*/\^=]"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("SKIP", r"[ \t]+"),
]

def tokenize(text):
    tokens = []
    pos = 0

    while pos < len(text):
        match = None

        for token_type, pattern in TOKEN_SPEC:
            regex = re.compile(pattern)
            match = regex.match(text, pos)

            if match:
                value = match.group(0)

                if token_type != "SKIP":
                    tokens.append((token_type, value))

                pos = match.end()
                break

        if not match:
            raise LexerError(f"Invalid character: {text[pos]}")

    return tokens
