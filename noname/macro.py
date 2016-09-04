from .parameter_spec import ParameterSpec


class Macro(object):
    def __init__(self, param_spec: ParameterSpec, body, env):
        self.param_spec = param_spec
        self.body = body
        self.env = env

# true, false (Boolean)
# nil Type
# def
# fn
# do
# macro <
# defn
# defmacro
# if
# when
# unless

