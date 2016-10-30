import sys
import traceback
try:
    import readline
except ImportError:
    readline = None

from noname import Environment
from noname import evaluate
from noname import parse
from noname import tokenize
from noname.builtin import builtin_env
from noname.describer import describe
from noname.exc import ExitError


def reader():
    while True:
        try:
            raw_string = input(">>> ")
            if readline is not None:
                readline.add_history(raw_string)
        except KeyboardInterrupt:
            print()
            print("KeyboardInterrupt")
            continue
        except EOFError:
            print()
            raise ExitError(1)
        for c in raw_string:
            yield c
        yield '\n'


def main(argv=sys.argv[1:]):
    env = Environment(builtin_env)
    try:
        while True:
            tokens = tokenize(reader())
            trees = parse(tokens)
            for tree in trees:
                try:
                    print(describe(evaluate(tree, env)))
                except ExitError:
                    raise
                except:
                    traceback.print_exception(*sys.exc_info())
    except ExitError as e:
        sys.exit(e.code)

if __name__ == '__main__':
    main()
