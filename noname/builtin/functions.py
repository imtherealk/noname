from ..environment import Environment
from ..native_code import native_code


@native_code
def list_body(env: Environment):
    return env.find_by_name('items')
