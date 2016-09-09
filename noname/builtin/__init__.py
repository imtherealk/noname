from noname.builtin import macros, functions
from noname.builtin.functions import from_native_function
from noname.types import Symbol
from .env import builtin_env

builtin_env.set(Symbol('true'), True)
builtin_env.set(Symbol('false'), False)
builtin_env.set(Symbol('nil'), None)
builtin_env.set(Symbol('quote'), macros.quote_macro)
builtin_env.set(Symbol('def'), macros.def_macro)
builtin_env.set(Symbol('fn'), macros.fn_macro)
builtin_env.set(Symbol('macro'), macros.macro_macro)
builtin_env.set(Symbol('list'), functions.list_function)
builtin_env.set(Symbol('defn'), macros.defn_macro)
builtin_env.set(Symbol('defmacro'), macros.defmacro_macro)
builtin_env.set(Symbol('do'), macros.do_macro)
# Simple builtin functions
builtin_env.set(Symbol('+'), functions.add_function)
builtin_env.set(Symbol('-'), functions.sub_function)
builtin_env.set(Symbol('*'), functions.mul_function)
builtin_env.set(Symbol('/'), functions.div_function)
builtin_env.set(Symbol('mod'), functions.mod_function)
builtin_env.set(Symbol('power'), functions.pow_function)
builtin_env.set(Symbol('sqrt'), functions.sqrt_function)
builtin_env.set(Symbol('first'), functions.first_function)
builtin_env.set(Symbol('rest'), functions.rest_function)
builtin_env.set(Symbol('take'), functions.take_function)
builtin_env.set(Symbol('drop'), functions.drop_function)
builtin_env.set(Symbol('take-last'), functions.take_last_function)
builtin_env.set(Symbol('drop-last'), functions.drop_last_function)
builtin_env.set(Symbol('concat'), functions.concat_function)
builtin_env.set(Symbol('append'), functions.append_function)
builtin_env.set(Symbol('println'), functions.println_function)
