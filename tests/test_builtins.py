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

        result = execute('''
            (fn (x y)
              (println x)
              (println y)
              (+ x y))
        ''', root_env)
        self.assertIsInstance(result, Function)
        self.assertEqual(ParameterSpec([Symbol('x'), Symbol('y')]),
                         result.param_spec)
        self.assertEqual(
            parse(tokenize('(do (println x) (println y) (+ x y))'))[0],
            result.body)
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

    def test_do(self):
        # body가 비어있을 때
        result = execute('''
            (do)
        ''')
        self.assertIsNone(result)
        # 마지막 expression을 return한다
        result = execute('''
            (do (+ 1 2) (+ 3 4))
        ''')
        self.assertEqual(7, result)
        # 순서대로 모든 expression을 evaluate한다
        execute('''
            (do
              (def a 1)
              (def b (+ a 1))
              (def c (+ b 1)))
        ''')
        self.assertEqual(1, root_env.find_by_name('a'))
        self.assertEqual(2, root_env.find_by_name('b'))
        self.assertEqual(3, root_env.find_by_name('c'))
        # 스코프 체크
        env = Environment(root_env)
        env.set_with_name('a', 5)
        result = execute('''
            (do (+ a 2))
        ''', env)
        self.assertEqual(7, result)


if __name__ == '__main__':
    unittest.main()
