from ..types import Symbol
from ..parameter_spec import ParameterSpec
from ..function import Function
from ..environment import Environment
from ..native_code import native_code


@native_code
def list_body(env: Environment):
    return env.find_by_name('items')


def from_native_function(native_function, env: Environment):
    @native_code
    def body(env: Environment):
        args = env.find_by_name('args')
        return native_function(*args)
    return Function(ParameterSpec([], Symbol('args')), body, env)
