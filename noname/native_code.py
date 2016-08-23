import abc


class NativeCode(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self, env):
        pass
