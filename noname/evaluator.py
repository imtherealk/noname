from . import parameter_spec
from .native_code import NativeCode
from .macro import Macro
from .environment import Environment
from .function import Function
from .types import Symbol


def evaluate(item, env):
    """Evaluate"""
    if isinstance(item, list):
        first = evaluate(item[0], env)
        if isinstance(first, Function):
            return call_function(first, item[1:], env)
        elif isinstance(first, Macro):
            return call_macro(first, item[1:], env)
        else:
            raise SyntaxError
    elif isinstance(item, Symbol):
        return env.find(item)
    elif isinstance(item, NativeCode):
        return item.run(env)
    else:
        return item


def call_function(function: Function, args, env):
    args = [evaluate(x, env) for x in args]
    new_env = Environment(function.env)

    parameter_spec.bind(new_env, function.param_spec, args)
    return evaluate(function.body, new_env)


def call_macro(macro: Macro, args, env):
    new_env = Environment(macro.env)
    parameter_spec.bind(new_env, macro.param_spec, args)
    generated_code = evaluate(macro.body, new_env)
    return evaluate(generated_code, env)
