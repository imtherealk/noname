import unittest

from noname import evaluate, Symbol
from noname.environment import Environment


class TestEvaluator(unittest.TestCase):
    def test_number(self):
        result = evaluate(1, Environment.from_dict({}))
        expected = 1
        self.assertEqual(expected, result)

    def test_string(self):
        result = evaluate('string', Environment.from_dict({}))
        expected = 'string'
        self.assertEqual(expected, result)

    def test_symbol(self):
        result = evaluate(Symbol('a'), Environment.from_dict({
            'a': 1
        }))
        expected = 1
        self.assertEqual(expected, result)

    def test_unknown(self):
        self.assertRaises(NameError, evaluate, Symbol('b'),
                          Environment.from_dict({
                              'a': 1
                          }))
