import math
import functools
import operator

from .env import builtin_env
from ..types import Symbol
from ..parameter_spec import ParameterSpec
from ..function import Function
from ..environment import Environment
from ..native_code import native_code


def function(positional_names, extra_name=None):
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
        return Function(param_spec, body, builtin_env)
    return decorator


@function([], 'items')
def list_function(items):
    return items


def from_native_function(native_function, env: Environment):
    @native_code
    def body(env: Environment):
        args = env.find_by_name('args')
        return native_function(*args)

    return Function(ParameterSpec([], Symbol('args')), body, env)


add_function = from_native_function(
    lambda *args: functools.reduce(operator.add, args),
    builtin_env)
sub_function = from_native_function(
    lambda *args: functools.reduce(operator.sub, args),
    builtin_env)
mul_function = from_native_function(
    lambda *args: functools.reduce(operator.mul, args),
    builtin_env)
div_function = from_native_function(
    lambda *args: functools.reduce(lambda x, y: x / y, args),
    builtin_env)
mod_function = from_native_function(operator.mod, builtin_env)
pow_function = from_native_function(math.pow, builtin_env)
sqrt_function = from_native_function(math.sqrt, builtin_env)
first_function = from_native_function(lambda x: x[0], builtin_env)
rest_function = from_native_function(lambda x: x[1:], builtin_env)
take_function = from_native_function(lambda n, x: x[:n], builtin_env)
drop_function = from_native_function(lambda n, x: x[n:], builtin_env)
take_last_function = from_native_function(lambda n, x: x[-n:], builtin_env)
drop_last_function = from_native_function(lambda n, x: x[:-n], builtin_env)
concat_function = from_native_function(lambda x, y: list(x) + list(y),
                                       builtin_env)
append_function = from_native_function(lambda x, y: list(x) + [y], builtin_env)
println_function = from_native_function(print, builtin_env)
