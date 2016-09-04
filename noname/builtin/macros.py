from .. import parameter_spec
from ..macro import Macro
from ..environment import Environment
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


@native_code
def fn_body(env):
    param_spec = env.find(Symbol('param_spec'))
    body = env.find(Symbol('body'))

    param_spec = parameter_spec.parse(param_spec)

    @native_code
    def inner(env):
        return Function(param_spec, body, env)

    return inner


@native_code
def macro_body(env):
    param_spec = env.find(Symbol('param_spec'))
    body = env.find(Symbol('body'))

    param_spec = parameter_spec.parse(param_spec)

    @native_code
    def inner(env):
        return Macro(param_spec, body, env)

    return inner


@native_code
def defn_body(env: Environment):
    name = env.find(Symbol('name'))
    param_spec = env.find(Symbol('param_spec'))
    body = env.find(Symbol('body'))
    return [Symbol('def'), name, [Symbol('fn'), param_spec, body]]


@native_code
def defmacro_body(env):
    name = env.find(Symbol('name'))
    param_spec = env.find(Symbol('param_spec'))
    body = env.find(Symbol('body'))
    return [Symbol('def'), name, [Symbol('macro'), param_spec, body]]
