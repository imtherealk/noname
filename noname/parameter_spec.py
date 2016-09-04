from .types import Symbol


class ParameterSpec(object):
    def __init__(self, positionals, extra=None):
        super().__init__()
        self.positionals = positionals
        self.extra = extra

    def __eq__(self, other):
        if not isinstance(other, ParameterSpec):
            return False
        return (self.positionals == other.positionals and
                self.extra == other.extra)

    def __repr__(self):
        positionals = ', '.join(x.name for x in self.positionals)
        extra = None
        if self.extra:
            extra = self.extra.name

        return 'ParameterSpec(positionals=[{0}], extra={1}'.format(
            positionals, extra)


def _assert_type(expected, actual):
    if not isinstance(actual, expected):
        raise TypeError("Expected type {0!r}, not {1!r}"
                        .format(expected, type(actual)))


def parse(param_spec_tree):
    _assert_type(list, param_spec_tree)

    positionals = []
    extra = None
    param_spec_tree = param_spec_tree.copy()

    while param_spec_tree and param_spec_tree[0] != Symbol('&'):
        _assert_type(Symbol, param_spec_tree[0])
        positionals.append(param_spec_tree.pop(0))

    if param_spec_tree and len(param_spec_tree) != 2:
        raise SyntaxError

    if param_spec_tree:
        extra = param_spec_tree[1]
        _assert_type(Symbol, extra)

    return ParameterSpec(positionals, extra)


def bind(env, param_spec: ParameterSpec, args):
    if len(args) < len(param_spec.positionals):
        raise TypeError("Expected at least {0} argument(s) ({1} given)"
                        .format(len(param_spec.positionals), len(args)))

    for name, arg in zip(param_spec.positionals, args):
        env.set(name, arg)

    if param_spec.extra is not None:
        env.set(param_spec.extra, args[len(param_spec.positionals):])
