from .parameter_spec import ParameterSpec


class Function(object):
    def __init__(self, param_spec: ParameterSpec, body, env):
        self.param_spec = param_spec
        self.body = body
        self.env = env
