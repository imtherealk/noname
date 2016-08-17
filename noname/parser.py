from .types import Symbol

PARENTHESES = ['(', ')']


def parse(tokens):
    result = []
    while tokens:
        result.append(read_single_set(tokens))
    return result


def read_single_set(tokens):
    token = tokens.pop(0)
    if token == '(':
        result = []
        while tokens[0] != ')':
            result.append(read_single_set(tokens))
        tokens.pop(0)
        return result
    # elif token == "'":
    #     pass
    elif token[0] == '"':
        chars = list(token)
        chars.pop(0)
        chars.pop(len(chars) - 1)
        return ''.join(chars)
    else:
        try:
            return int(token)
        except ValueError:
            try:
                return float(token)
            except ValueError:
                return Symbol(token)

