import math
import functools
import operator

from noname.builtin import macros, functions
from noname.builtin.functions import from_native_function
from noname.function import Function
from noname.macro import Macro
from noname.parameter_spec import ParameterSpec
from noname.types import Symbol
from noname.environment import Environment

root_env = Environment(None)
root_env.set(Symbol('true'), True)
root_env.set(Symbol('false'), False)
root_env.set(Symbol('nil'), None)
root_env.set(Symbol('def'),
             Macro(ParameterSpec([Symbol('name'), Symbol('value')]),
                   macros.def_body,
                   root_env))
root_env.set(Symbol('fn'),
             Macro(ParameterSpec([Symbol('param_spec')], Symbol('bodies')),
                   macros.fn_body,
                   root_env))
root_env.set(Symbol('macro'),
             Macro(ParameterSpec([Symbol('param_spec')], Symbol('bodies')),
                   macros.macro_body,
                   root_env))
root_env.set(Symbol('list'),
             Function(ParameterSpec([], Symbol('items')),
                      functions.list_body,
                      root_env))
root_env.set(Symbol('defn'),
             Macro(ParameterSpec([
                 Symbol('name'),
                 Symbol('param_spec')],
                 Symbol('bodies')),
                 macros.defn_body, root_env))
root_env.set(Symbol('defmacro'),
             Macro(ParameterSpec([
                 Symbol('name'),
                 Symbol('param_spec')],
                 Symbol('bodies')),
                 macros.defmacro_body, root_env))
root_env.set(Symbol('do'),
             Macro(ParameterSpec([], Symbol('bodies')),
                   macros.do_body,
                   root_env))
# Simple builtin functions
root_env.set(Symbol('+'),
             from_native_function(
                 lambda *args: functools.reduce(operator.add, args),
                 root_env))
root_env.set(Symbol('-'),
             from_native_function(
                 lambda *args: functools.reduce(operator.sub, args),
                 root_env))
root_env.set(Symbol('*'),
             from_native_function(
                 lambda *args: functools.reduce(operator.mul, args),
                 root_env))
root_env.set(Symbol('/'),
             from_native_function(
                 lambda *args: functools.reduce(lambda x, y: x / y, args),
                 root_env))
root_env.set(Symbol('mod'), from_native_function(operator.mod, root_env))
root_env.set(Symbol('power'), from_native_function(math.pow, root_env))
root_env.set(Symbol('sqrt'), from_native_function(math.sqrt, root_env))
root_env.set(Symbol('first'),
             from_native_function(lambda x: x[0], root_env))
root_env.set(Symbol('rest'),
             from_native_function(lambda x: x[1:], root_env))
root_env.set(Symbol('take'),
             from_native_function(lambda n, x: x[:n], root_env))
root_env.set(Symbol('drop'),
             from_native_function(lambda n, x: x[n:], root_env))
root_env.set(Symbol('take-last'),
             from_native_function(lambda n, x: x[-n:], root_env))
root_env.set(Symbol('drop-last'),
             from_native_function(lambda n, x: x[:-n], root_env))
root_env.set(Symbol('concat'),
             from_native_function(lambda x, y: list(x) + list(y), root_env))
root_env.set(Symbol('append'),
             from_native_function(lambda x, y: list(x) + [y], root_env))
root_env.set(Symbol('println'),
             from_native_function(print, root_env))
