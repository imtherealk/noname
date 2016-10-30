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
            yield from self.next_item()

    def next_item(self):
        if self.first == '(':
            yield from self.next_list()
        elif self.first == "'":
            yield from self.next_quote()
        elif self.first[0] == '"':
            yield from self.next_string()
        elif self.first[0].isdigit():
            yield from self.next_number()
        else:
            yield from self.next_symbol()

    def sync_next_item(self):
        return list(self.next_item())[0]

    def next_list(self):
        # (+ 1 2)
        self.read_token()
        result = []
        while self.first != ')':
            result.append(self.sync_next_item())
        yield result
        self.read_token()

    def next_string(self):
        token = self.first
        yield unescape_string(token[1:-1])
        self.read_token()

    def next_number(self):
        token = self.first
        try:
            yield int(token)
        except ValueError:
            yield float(token)
        self.read_token()

    def next_symbol(self):
        symbol = Symbol(self.first)
        yield symbol
        self.read_token()

    def next_quote(self):
        self.read_token()
        item = self.sync_next_item()
        yield [Symbol('quote'), item]

    def read_token(self):
        try:
            self.first = next(self.tokens)
        except StopIteration:
            self.first = None
            self.finished = True
