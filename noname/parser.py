from .types import Symbol
from .helpers import unescape_string

PARENTHESES = ['(', ')']


def parse(tokens):
    result = []
    while tokens:
        result.append(next_item(tokens))
    return result


def next_item(tokens):
    token = tokens[0]
    if token == '(':
        return next_list(tokens)
    # elif token == "'":
    #     pass
    elif token[0] == '"':
        return next_string(tokens)
    elif token[0].isdigit():
        return next_number(tokens)
    else:
        return next_symbol(tokens)


def next_list(tokens):
    result = []
    tokens.pop(0)
    while tokens[0] != ')':
        result.append(next_item(tokens))
    tokens.pop(0)
    return result


def next_string(tokens):
    token = tokens.pop(0)
    return unescape_string(token[1:-1])


def next_number(tokens):
    token = tokens.pop(0)
    try:
        return int(token)
    except ValueError:
        return float(token)


def next_symbol(tokens):
    token = tokens.pop(0)
    return Symbol(token)
