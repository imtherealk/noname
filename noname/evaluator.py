from .native_code import NativeCode
from .macro import Macro, bind
from .environment import Environment
from .function import Function
from .types import Symbol


def evaluate(item, env):
    """Evalute"""
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


def call_function(function, args, env):
    evaluated_args = []

    for arg in args:
        evaluated_args.append(evaluate(arg, env))
    new_env = Environment(function.env)

    for i, name in enumerate(function.param_names):
        new_env.set(name, evaluated_args[i])

    return evaluate(function.body, new_env)


def call_macro(macro, args, env):
    new_env = Environment(macro.env)

    for i, name in enumerate(macro.param_names):
        new_env.set(name, args[i])

    generated_code = evaluate(macro.body, new_env)
    return evaluate(generated_code, env)

