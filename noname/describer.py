from noname.function import Function
from noname.helpers import escape_string
from noname.macro import Macro
from noname.native_code import NativeCode
from noname.types import Symbol


def describe(item, env):
    if isinstance(item, list):
        return describe_list(item, env)
    elif isinstance(item, Symbol):
        return describe_symbol(item, env)
    elif isinstance(item, str):
        return describe_str(item, env)
    elif isinstance(item, (int, float)):
        return describe_number(item, env)
    elif isinstance(item, Macro):
        return describe_macro(item, env)
    elif isinstance(item, Function):
        return describe_function(item, env)
    elif isinstance(item, NativeCode):
        return describe_native(item, env)
    else:
        pass


def describe_list(item, env):
    return '(' + ' '.join(describe(x, env) for x in item) + ')'


def describe_symbol(item, env):
    return item.name


def describe_str(item, env):
    return '"' + escape_string(item) + '"'


def describe_number(item, env):
    return str(item)


def describe_macro(item, env):
    name = env.find_name(item)
    if name is None:
        name = id(item)
    return "<Macro: {}>".format(name)


def describe_function(item, env):
    name = env.find_name(item)
    if name is None:
        name = id(item)
    return "<Function: {}>".format(name)


def describe_native(item, env):
    return "<NativeCode: {}>".format(id(item))
