from noname.builtin import macros, functions
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
             Macro(ParameterSpec([Symbol('param_spec'), Symbol('body')]),
                   macros.fn_body,
                   root_env))
root_env.set(Symbol('macro'),
             Macro(ParameterSpec([Symbol('param_spec'), Symbol('body')]),
                   macros.macro_body,
                   root_env))
root_env.set(Symbol('list'),
             Function(ParameterSpec([], Symbol('items')),
                      functions.list_body,
                      root_env))
root_env.set(Symbol('defn'),
             Macro(ParameterSpec([
                 Symbol('name'),
                 Symbol('param_spec'),
                 Symbol('body')
             ]), macros.defn_body, root_env))
root_env.set(Symbol('defmacro'),
             Macro(ParameterSpec([
                 Symbol('name'),
                 Symbol('param_spec'),
                 Symbol('body')
             ]), macros.defmacro_body, root_env))
