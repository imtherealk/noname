import unittest

from noname import evaluate, Symbol


class TestEvaluator(unittest.TestCase):
    def test_number(self):
        result = evaluate(1, {})
        expected = 1
        self.assertEqual(expected, result)

    def test_string(self):
        result = evaluate('string', {})
        expected = 'string'
        self.assertEqual(expected, result)

    def test_symbol(self):
        result = evaluate(Symbol('a'), {
            'a': 1
        })
        expected = 1
        self.assertEqual(expected, result)

    def test_unknown(self):
        self.assertRaises(RuntimeError, evaluate, Symbol('b'), {
            'a': 1
        })
