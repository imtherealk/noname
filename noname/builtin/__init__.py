from noname.builtin import macros
from noname.macro import Macro
from noname.types import Symbol
from noname.environment import Environment

root_env = Environment(None)
root_env.set(Symbol('true'), True)
root_env.set(Symbol('false'), False)
root_env.set(Symbol('nil'), None)
root_env.set(Symbol('def'), Macro([Symbol('name'), Symbol('value')],
                                  macros.def_body,
                                  root_env))
root_env.set(Symbol('fn'), Macro([Symbol('names'), Symbol('body')],
                                 macros.fn_body,
                                 root_env))
root_env.set(Symbol('macro'), Macro([Symbol('names'), Symbol('body')],
                                    macros.macro_body,
                                    root_env))
