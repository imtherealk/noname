from .env import builtin_env
from ..parameter_spec import ParameterSpec
from .. import parameter_spec
from ..macro import Macro
from ..environment import Environment
from ..function import Function
from ..evaluator import evaluate
from ..native_code import native_code
from ..types import Symbol


def combine_expressions(expressions):
    if not expressions:
        return None
    elif len(expressions) == 1:
        return expressions[0]
    else:
        return [do_macro] + expressions


def macro(positional_names, extra_name=None):
    positionals = [Symbol(x) for x in positional_names]
    if extra_name is not None:
        extra = Symbol(extra_name)
    else:
        extra = None

    param_spec = ParameterSpec(positionals, extra)

    def decorator(fn):
        @native_code
        def body(env):
            arguments = {}
            param_names = []
            for positional in positional_names:
                param_names.append(positional)
            if extra_name is not None:
                param_names.append(extra_name)
            for name in param_names:
                arguments[name] = env.find_by_name(name)
            return fn(**arguments)
        return Macro(param_spec, body, builtin_env)
    return decorator


@macro(['name', 'param_spec'], 'bodies')
def defn_macro(name, param_spec, bodies):
    return [def_macro, name, [fn_macro, param_spec] + bodies]


@macro(['name', 'value'])
def def_macro(name, value):
    @native_code
    def inner(env: Environment):
        root_env = env
        while root_env.parent.parent is not None:
            root_env = root_env.parent
        root_env.set(name, evaluate(value, env))
        return None

    return inner


@macro(['value'])
def quote_macro(value):
    @native_code
    def inner(env):
        return value

    return inner


@macro(['param_spec'], 'bodies')
def fn_macro(param_spec, bodies):
    body = combine_expressions(bodies)
    param_spec = parameter_spec.parse(param_spec)

    @native_code
    def inner(env):
        return Function(param_spec, body, env)

    return inner


@macro(['param_spec'], 'bodies')
def macro_macro(param_spec, bodies):
    body = combine_expressions(bodies)
    param_spec = parameter_spec.parse(param_spec)

    @native_code
    def inner(env):
        return Macro(param_spec, body, env)

    return inner


@macro(['name', 'param_spec'], 'bodies')
def defmacro_macro(name, param_spec, bodies):
    body = combine_expressions(bodies)
    return [def_macro, name, [macro_macro, param_spec, body]]


@macro([], 'bodies')
def do_macro(bodies):
    @native_code
    def inner(env):
        result = None
        for body in bodies:
            result = evaluate(body, env)
        return result

    return inner
