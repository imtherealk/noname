import unittest

from noname import execute, parse, tokenize
from noname.parameter_spec import ParameterSpec
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
        self.assertEqual(ParameterSpec([Symbol('x'), Symbol('y')]),
                         result.param_spec)
        self.assertEqual(parse(tokenize('(+ 1 (+ x y)))'))[0], result.body)
        self.assertEqual(root_env, result.env)

    def test_macro(self):
        result = execute('''
            (macro (x y) (+ 1 (+ x y)))
        ''', root_env)
        self.assertIsInstance(result, Macro)
        self.assertEqual(ParameterSpec([Symbol('x'), Symbol('y')]),
                         result.param_spec)
        self.assertEqual(parse(tokenize('(+ 1 (+ x y)))'))[0], result.body)
        self.assertEqual(root_env, result.env)

    def test_defn(self):
        env = Environment(root_env)
        result = execute('''
            (defn inc (x) (+ 1 x))
        ''', env)
        self.assertIsNone(result)
        inc = root_env.find_by_name('inc')
        self.assertIsInstance(inc, Function)
        self.assertEqual(ParameterSpec([Symbol('x')]), inc.param_spec)
        self.assertEqual(parse(tokenize('(+ 1 x)'))[0], inc.body)
        self.assertEqual(env, inc.env)

    def test_defmacro(self):
        env = Environment(root_env)
        result = execute('''
            (defmacro defadded
              (name first second)
              (list 'def name (list + first second)))
        ''', env)
        self.assertIsNone(result)
        defadded = root_env.find_by_name('defadded')
        self.assertIsInstance(defadded, Macro)
        self.assertEqual(
            ParameterSpec([Symbol('name'), Symbol('first'), Symbol('second')]),
            defadded.param_spec)
        self.assertEqual(
            parse(tokenize("(list 'def name (list + first second))"))[0],
            defadded.body)
        self.assertEqual(env, defadded.env)


if __name__ == '__main__':
    unittest.main()
