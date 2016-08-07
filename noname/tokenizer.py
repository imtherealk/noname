import string


def skip_whitespaces(chars):
    while chars and chars[0] in string.whitespace:
        chars.pop(0)


def next_number(chars):
    number = chars.pop(0)
    while chars[0].isdigit():
        number += chars.pop(0)
    return number


def next_symbol(chars):
    symbol = chars.pop(0)
    while chars[0] not in ['(', ')'] + list(string.whitespace):
        symbol += chars.pop(0)
    return symbol


def next_token(chars):
    skip_whitespaces(chars)
    if not chars:
        return

    ch = chars[0]
    if ch in ['(', ')']:
        return chars.pop(0)
    elif ch.isdigit():
        return next_number(chars)
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

    while chars:
        ch = chars[0]
        if ch == '(' or ch == ')':
            tokens.append(chars.pop(0))
        elif ch.isdigit():
            number = chars.pop(0)
            while chars[0].isdigit():
                number += chars.pop(0)
            tokens.append(number)
        elif ch in string.whitespace:
            chars.pop(0)
            while chars[0] in string.whitespace:
                chars.pop(0)
        else:
            symbol = chars.pop(0)
            while not (chars[0] == '(' or chars[0] == ')' or chars[0] in string.whitespace):
                symbol += chars.pop(0)
            tokens.append(symbol)
    return tokens
