import string


SINGLE_TOKENS = ['(', ')', "'"]


def skip_whitespaces(chars):
    while chars and chars[0] in string.whitespace:
        chars.pop(0)


def next_number(chars):
    number = chars.pop(0)
    while chars and chars[0].isdigit():
        number += chars.pop(0)
    return number


def next_string(chars):
    token = chars.pop(0)
    while chars[0] != '"':
        token += chars.pop(0)
    token += chars.pop(0)
    return token


def next_full_number(chars):
    left = next_number(chars)
    if chars and chars[0] == '.':
        number = left + chars.pop(0) + next_number(chars)
    else:
        number = left
    return number


def next_symbol(chars):
    symbol = chars.pop(0)
    while chars and chars[0] not in SINGLE_TOKENS + list(string.whitespace):
        symbol += chars.pop(0)
    return symbol


def next_token(chars):
    skip_whitespaces(chars)
    if not chars:
        return

    ch = chars[0]
    if ch in SINGLE_TOKENS:
        return chars.pop(0)
    elif ch.isdigit():
        return next_full_number(chars)
    elif ch == '"':
        return next_string(chars)
    else:
        return next_symbol(chars)


def tokenize(source):
    tokens = []
    chars = list(source)

    while True:
        token = next_token(chars)
        if token is None:
            break
        tokens.append(token)
    return tokens
