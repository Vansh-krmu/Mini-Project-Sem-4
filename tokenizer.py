# tokenizer.py

import re
from errors import LexerError


def tokenize(text):
    tokens = []

    token_specification = [
        ("NUMBER", r"\d+(\.\d+)?"),
        ("FUNC", r"sin|cos|tan|sqrt|log"),        
        ("IDENT", r"[a-zA-Z_]\w*"),                
        ("OP", r"[\+\-\*/\^=]"),               
        ("LPAREN", r"\("),                     
        ("RPAREN", r"\)"),                        
        ("SKIP", r"[ \t]+"),                     
        ("MISMATCH", r"."),                     

    tok_regex = "|".join(
        f"(?P<{name}>{pattern})"
        for name, pattern in token_specification
    )

    for match in re.finditer(tok_regex, text):
        kind = match.lastgroup
        value = match.group()

        if kind == "NUMBER":
            tokens.append(("NUMBER", value))

        elif kind == "FUNC":
            tokens.append(("FUNC", value))

        elif kind == "IDENT":
            tokens.append(("IDENT", value))

        elif kind == "OP":
            tokens.append(("OP", value))

        elif kind == "LPAREN":
            tokens.append(("LPAREN", value))

        elif kind == "RPAREN":
            tokens.append(("RPAREN", value))

        elif kind == "SKIP":
            continue

        elif kind == "MISMATCH":
            raise LexerError(
                f"Unexpected character: {value}"
            )

    return tokens
