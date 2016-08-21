from .types import Symbol


def evaluate(item, env):
    """Evalute"""
    if isinstance(item, int):
        return item
    elif isinstance(item, str):
        return item
    elif isinstance(item, Symbol):
        try:
            return env[item.name]
        except:
            raise RuntimeError
