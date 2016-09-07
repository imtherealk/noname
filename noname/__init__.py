from .tokenizer import tokenize
from .parser import parse
from .evaluator import evaluate
from .types import Symbol
from .environment import Environment


def execute(code, env: Environment):
    expressions = parse(tokenize(code))
    result = None
    for expression in expressions:
        result = evaluate(expression, env)
    return result


__all__ = ['tokenize', 'parse', 'evaluate', 'Symbol', 'Environment']
