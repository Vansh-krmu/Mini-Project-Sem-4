import re

TOKEN_REGEX = [
    ("NUMBER", r"\d+(\.\d+)?"),
    ("FUNC", r"sin|cos|tan"),
    ("IDENT", r"[a-zA-Z]+"),
    ("OP", r"[+\-*/=]"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("SKIP", r"[ \t]+"),
]


def tokenize(text):
    tokens = []
    while text:
        for token_type, regex in TOKEN_REGEX:
            match = re.match(regex, text)
            if match:
                value = match.group(0)
                if token_type != "SKIP":
                    tokens.append((token_type, value))
                text = text[len(value):]
                break
        else:
            raise Exception(f"Invalid character: {text[0]}")
    return tokens