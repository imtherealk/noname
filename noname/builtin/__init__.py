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

builtin_env = Environment(None)
builtin_env.set(Symbol('true'), True)
builtin_env.set(Symbol('false'), False)
builtin_env.set(Symbol('nil'), None)
builtin_env.set(Symbol('quote'),
                Macro(ParameterSpec([Symbol('value')]),
                      macros.quote_body,
                      builtin_env))
builtin_env.set(Symbol('def'),
                Macro(ParameterSpec([Symbol('name'), Symbol('value')]),
                      macros.def_body,
                      builtin_env))
builtin_env.set(Symbol('fn'),
                Macro(ParameterSpec([Symbol('param_spec')], Symbol('bodies')),
                      macros.fn_body,
                      builtin_env))
builtin_env.set(Symbol('macro'),
                Macro(ParameterSpec([Symbol('param_spec')], Symbol('bodies')),
                      macros.macro_body,
                      builtin_env))
builtin_env.set(Symbol('list'),
                Function(ParameterSpec([], Symbol('items')),
                         functions.list_body,
                         builtin_env))
builtin_env.set(Symbol('defn'),
                Macro(ParameterSpec([
                    Symbol('name'),
                    Symbol('param_spec')],
                    Symbol('bodies')),
                    macros.defn_body, builtin_env))
builtin_env.set(Symbol('defmacro'),
                Macro(ParameterSpec([
                    Symbol('name'),
                    Symbol('param_spec')],
                    Symbol('bodies')),
                    macros.defmacro_body, builtin_env))
builtin_env.set(Symbol('do'),
                Macro(ParameterSpec([], Symbol('bodies')),
                      macros.do_body,
                      builtin_env))
# Simple builtin functions
builtin_env.set(Symbol('+'),
                from_native_function(
                    lambda *args: functools.reduce(operator.add, args),
                    builtin_env))
builtin_env.set(Symbol('-'),
                from_native_function(
                    lambda *args: functools.reduce(operator.sub, args),
                    builtin_env))
builtin_env.set(Symbol('*'),
                from_native_function(
                    lambda *args: functools.reduce(operator.mul, args),
                    builtin_env))
builtin_env.set(Symbol('/'),
                from_native_function(
                    lambda *args: functools.reduce(lambda x, y: x / y, args),
                    builtin_env))
builtin_env.set(Symbol('mod'), from_native_function(operator.mod, builtin_env))
builtin_env.set(Symbol('power'), from_native_function(math.pow, builtin_env))
builtin_env.set(Symbol('sqrt'), from_native_function(math.sqrt, builtin_env))
builtin_env.set(Symbol('first'),
                from_native_function(lambda x: x[0], builtin_env))
builtin_env.set(Symbol('rest'),
                from_native_function(lambda x: x[1:], builtin_env))
builtin_env.set(Symbol('take'),
                from_native_function(lambda n, x: x[:n], builtin_env))
builtin_env.set(Symbol('drop'),
                from_native_function(lambda n, x: x[n:], builtin_env))
builtin_env.set(Symbol('take-last'),
                from_native_function(lambda n, x: x[-n:], builtin_env))
builtin_env.set(Symbol('drop-last'),
                from_native_function(lambda n, x: x[:-n], builtin_env))
builtin_env.set(Symbol('concat'),
                from_native_function(lambda x, y: list(x) + list(y), builtin_env))
builtin_env.set(Symbol('append'),
                from_native_function(lambda x, y: list(x) + [y], builtin_env))
builtin_env.set(Symbol('println'),
                from_native_function(print, builtin_env))
