import unittest

from noname import execute, parse, tokenize
from noname.types import Symbol
from noname.builtin import root_env
from noname.environment import Environment
from noname.function import Function
from noname.macro import Macro


class TestBuiltins(unittest.TestCase):
    def test_def(self):
        env = Environment(root_env)
        execute('''
            (def a 1)
        ''', env)
        self.assertEqual(1, env.find_by_name('a'))
        execute('''
            (def b a)
        ''', env)
        self.assertEqual(1, env.find_by_name('b'))

    def test_fn(self):
        result = execute('''
            (fn (x y) (+ 1 (+ x y)))
        ''', root_env)
        self.assertIsInstance(result, Function)
        self.assertEqual([Symbol('x'), Symbol('y')], result.param_names)
        self.assertEqual(parse(tokenize('(+ 1 (+ x y)))'))[0], result.body)
        self.assertEqual(root_env, result.env)

    def test_macro(self):
        result = execute('''
            (macro (x y) (+ 1 (+ x y)))
        ''', root_env)
        self.assertIsInstance(result, Macro)
        self.assertEqual([Symbol('x'), Symbol('y')], result.param_names)
        self.assertEqual(parse(tokenize('(+ 1 (+ x y)))'))[0], result.body)
        self.assertEqual(root_env, result.env)


if __name__ == '__main__':
    unittest.main()
