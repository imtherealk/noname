class Symbol(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Symbol):
            return False
        return self.name == other.name

    def __repr__(self):
        return 'Symbol(name={0!r})'.format(self.name)
