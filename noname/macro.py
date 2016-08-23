class Macro(object):
    def __init__(self, param_names, body, env):
        self.param_names = param_names
        self.body = body
        self.env = env
