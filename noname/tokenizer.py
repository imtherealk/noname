import string


SINGLE_TOKENS = ['(', ')', "'"]


def next_char(chars):
    try:
        return next(chars)
    except StopIteration:
        return None


def skip_whitespaces(first, chars):
    while first is not None and first in string.whitespace:
        first = next_char(chars)
    return first


def next_number(first, chars):
    number = first
    first = next_char(chars)
    while first is not None and first.isdigit():
        number += first
        first = next_char(chars)
    return first, number


def next_string(first, chars):
    token = first
    first = next_char(chars)
    while first != '"':
        if first == '\\':
            token += first
            first = next_char(chars)
        token += first
        first = next_char(chars)
    token += first
    first = next_char(chars)
    return first, token


def next_full_number(first, chars):
    first, left = next_number(first, chars)
    if first is not None and first == '.':
        first = next_char(chars)
        if first is None or not first.isdigit():
            number = left + '.'
        else:
            first, right = next_number(first, chars)
            number = left + '.' + right
    else:
        number = left
    return first, number


def next_symbol(first, chars):
    symbol = first
    nonsymbol_chars = SINGLE_TOKENS + list(string.whitespace) + ['"']
    first = next_char(chars)
    while first is not None and first not in nonsymbol_chars:
        symbol += first
        first = next_char(chars)
    return first, symbol


def next_token(first, chars):
    first = skip_whitespaces(first, chars)

    if first is None:
        return None, None

    if first in SINGLE_TOKENS:
        token = first
        first = next_char(chars)
        return first, token
    elif first.isdigit():
        return next_full_number(first, chars)
    elif first == '"':
        return next_string(first, chars)
    else:
        return next_symbol(first, chars)


def tokenize(source):
    source = iter(source)
    first = next(source)
    while first is not None:
        first, token = next_token(first, source)
        if token is None:
            break
        yield token
