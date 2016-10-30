from .types import Symbol
from .helpers import unescape_string

PARENTHESES = ['(', ')']


def parse(tokens):
    parser = Parser(iter(tokens))
    return parser.parse()


class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.first = None
        self.finished = False

    def parse(self):
        self.read_token()
        while not self.finished:
            yield self.next_item()

    def next_item(self):
        if self.first == '(':
            return self.next_list()
        elif self.first == "'":
            return self.next_quote()
        elif self.first[0] == '"':
            return self.next_string()
        elif self.first[0].isdigit():
            return self.next_number()
        else:
            return self.next_symbol()

    def next_list(self):
        self.read_token()
        result = []
        while self.first != ')':
            result.append(self.next_item())
        self.read_token()
        return result

    def next_string(self):
        token = self.first
        self.read_token()
        return unescape_string(token[1:-1])

    def next_number(self):
        token = self.first
        self.read_token()
        try:
            return int(token)
        except ValueError:
            return float(token)

    def next_symbol(self):
        symbol = Symbol(self.first)
        self.read_token()
        return symbol

    def next_quote(self):
        self.read_token()
        item = self.next_item()
        return [Symbol('quote'), item]

    def read_token(self):
        try:
            self.first = next(self.tokens)
        except StopIteration:
            self.first = None
            self.finished = True
