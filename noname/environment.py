from noname.types import Symbol


class Environment(object):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.variables = {}

    def find_by_name(self, name):
        return self.find(Symbol(name))

    def set_with_name(self, name, value):
        return self.set(Symbol(name), value)

    def find(self, name):
        if name.name in self.variables:
            return self.variables[name.name]
        elif self.parent is None:
            raise NameError(name.name)
        else:
            return self.parent.find(name)

    def set(self, name, value):
        self.variables[name.name] = value

    @classmethod
    def from_dict(cls, d, parent=None):
        env = cls(parent)
        for key, value in d.items():
            env.set(Symbol(key), value)
        return env
