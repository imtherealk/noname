from noname.function import Function
from noname.helpers import escape_string
from noname.macro import Macro
from noname.native_code import NativeCode
from noname.types import Symbol


def describe(item):
    if isinstance(item, list):
        return describe_list(item)
    elif isinstance(item, Symbol):
        return describe_symbol(item)
    elif isinstance(item, str):
        return describe_str(item)
    elif isinstance(item, (int, float)):
        return describe_number(item)
    elif isinstance(item, Macro):
        return describe_macro(item)
    elif isinstance(item, Function):
        return describe_function(item)
    elif isinstance(item, NativeCode):
        return describe_native(item)
    else:
        pass


def describe_list(item):
    return '(' + ' '.join(describe(x) for x in item) + ')'


def describe_symbol(item):
    return item.name


def describe_str(item):
    return '"' + escape_string(item) + '"'


def describe_number(item):
    return str(item)


def describe_macro(item):
    return "<Macro: {}>".format(id(item))


def describe_function(item):
    return "<Function: {}>".format(id(item))


def describe_native(item):
    return "<NativeCode: {}>".format(id(item))
