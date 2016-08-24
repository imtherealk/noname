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
