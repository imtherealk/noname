import string


SINGLE_TOKENS = ['(', ')', "'"]


def tokenize(source):
    tokenizer = Tokenizer(iter(source))
    return tokenizer.tokenize()


class Tokenizer(object):
    def __init__(self, chars):
        self.chars = chars
        self.first = None
        self.finished = False

    def tokenize(self):
        self.read_char()
        while not self.finished:
            token = self.next_token()
            if token is None:
                break
            yield token

    def read_char(self):
        try:
            self.first = next(self.chars)
        except StopIteration:
            self.first = None
            self.finished = True

    def skip_whitespaces(self):
        while not self.finished and self.first in string.whitespace:
            self.read_char()

    def next_number(self):
        number = self.first
        self.read_char()
        while not self.finished and self.first.isdigit():
            number += self.first
            self.read_char()
        return number

    def next_string(self):
        token = self.first
        self.read_char()
        while self.first != '"':
            if self.first == '\\':
                token += self.first
                self.read_char()
            token += self.first
            self.read_char()
        token += self.first
        self.read_char()
        return token

    def next_full_number(self):
        left = self.next_number()
        if not self.finished and self.first == '.':
            self.read_char()
            if self.finished or not self.first.isdigit():
                number = left + '.'
            else:
                right = self.next_number()
                number = left + '.' + right
        else:
            number = left
        return number

    def next_symbol(self):
        symbol = self.first
        nonsymbol_chars = SINGLE_TOKENS + list(string.whitespace) + ['"']
        self.read_char()
        while not self.finished and self.first not in nonsymbol_chars:
            symbol += self.first
            self.read_char()
        return symbol

    def next_token(self):
        self.skip_whitespaces()

        if self.finished:
            return None

        if self.first in SINGLE_TOKENS:
            token = self.first
            self.read_char()
            return token
        elif self.first.isdigit():
            return self.next_full_number()
        elif self.first == '"':
            return self.next_string()
        else:
            return self.next_symbol()

