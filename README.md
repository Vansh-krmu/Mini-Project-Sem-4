# Mini Math Interpreter

A Python-based interpreter that safely parses and evaluates mathematical expressions while preserving correct operator precedence — without using `eval()`.

## Features

- Parses mathematical expressions from strings
- Supports `+`, `-`, `*`, `/`, and parentheses
- Preserves operator precedence (PEMDAS)
- Builds and evaluates an Abstract Syntax Tree (AST)
- Provides clear and readable error messages
- Optional AST visualization for debugging

## Example

Input: `3 + 4 * 2`

Output: `11`


## How It Works

1. **Tokenization**  
   Converts the input string into tokens such as numbers, operators, and parentheses.

2. **Parsing**  
   Builds an Abstract Syntax Tree (AST) that represents the correct order of operations.

3. **Evaluation**  
   Recursively evaluates the AST to produce the final result.

4. **Error Handling**  
   Detects invalid characters, syntax errors, and mismatched parentheses.

## Use Cases

- Learning interpreter and parser fundamentals
- Understanding tokenization, parsing, and ASTs
- Academic or demonstration projects
- Safe alternative to `eval()` for math expressions

## Tech Stack

- Python
- Recursive Descent Parsing
- Abstract Syntax Trees (AST)

## License

Educational purposes **only**.
