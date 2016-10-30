import sys

from noname import Environment
from noname import evaluate
from noname import parse
from noname import tokenize
from noname.builtin import builtin_env
from noname.describer import describe


def reader():
    while True:
        raw_string = input(">>> ")
        for c in raw_string:
            yield c
        yield '\n'


def main(argv=sys.argv[1:]):
    env = Environment(builtin_env)
    while True:
        tokens = tokenize(reader())
        trees = parse(tokens)
        for tree in trees:
            print(describe(evaluate(tree, env)))

if __name__ == '__main__':
    main()
