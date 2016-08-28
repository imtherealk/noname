from ..macro import Macro
from ..function import Function
from ..evaluator import evaluate
from ..native_code import native_code
from ..types import Symbol


@native_code
def def_body(env):
    name = env.find(Symbol('name'))
    value = env.find(Symbol('value'))
    root_env = env.parent

    @native_code
    def inner(env):
        root_env.set(name, evaluate(value, env))
        return None

    return inner


def as_param_spec(param_spec):
    pass


@native_code
def fn_body(env):
    names = env.find(Symbol('names'))
    body = env.find(Symbol('body'))

    @native_code
    def inner(env):
        return Function(names, body, env)

    return inner


@native_code
def macro_body(env):
    names = env.find(Symbol('names'))
    body = env.find(Symbol('body'))

    @native_code
    def inner(env):
        return Macro(names, body, env)

    return inner
