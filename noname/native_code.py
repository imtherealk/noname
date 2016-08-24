import abc


class NativeCode(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self, env):
        pass


class WrapperCode(NativeCode):
    def __init__(self, fn):
        super().__init__()
        self.fn = fn

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def run(self, env):
        return self.fn(env)


def native_code(fn):
    return WrapperCode(fn)

