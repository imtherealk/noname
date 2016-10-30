import unittest

from noname import tokenize, parse, Symbol


class TestParser(unittest.TestCase):
    def test_simple(self):
        # (+ 1 2)
        tokens = ['(', '+', '1', '2', ')']

        ast = list(parse(tokens))
        expected = [
            [Symbol('+'), 1, 2]
        ]
        self.assertEqual(expected, ast)

    def test_nil(self):
        # ()
        tokens = ['(', ')']

        ast = list(parse(tokens))
        expected = [
            []
        ]
        self.assertEqual(expected, ast)

    def test_nested(self):
        # (* 2 (+ 1 2))
        tokens = tokenize('(* 2 (+ 1 2))')

        ast = list(parse(tokens))
        expected = [
            [Symbol('*'), 2, [Symbol('+'), 1, 2]]
        ]
        self.assertEqual(expected, ast)

    def test_string(self):
        # "string"
        tokens = ['"string"']

        ast = list(parse(tokens))
        expected = [
            "string"
        ]
        self.assertEqual(expected, ast)

    def test_escape(self):
        # "string\n\""
        tokens = [r'"string\n\""']

        ast = list(parse(tokens))
        expected = [
            "string\n\""
        ]
        self.assertEqual(expected, ast)

    def test_multiple(self):
        # (+ 1 2)(+ 3 4)
        tokens = tokenize('(+ 1 2)(+ 3 4)')

        ast = list(parse(tokens))
        expected = [
            [Symbol('+'), 1, 2],
            [Symbol('+'), 3, 4]
        ]
        self.assertEqual(expected, ast)

    def test_quote(self):
        # 'foo == (quote foo)
        tokens = ["'", 'foo']

        ast = list(parse(tokens))
        expected = [
            [Symbol('quote'), Symbol('foo')]
        ]
        self.assertEqual(expected, ast)

    def test_list_quote(self):
        # '(+ 1 2) == (quote (+ 1 2))
        tokens = ["'", '(', '+', '1', '2', ')']

        ast = list(parse(tokens))
        expected = [
            [Symbol('quote'), [Symbol('+'), 1, 2]]
        ]
        self.assertEqual(expected, ast)

    def test_nested_quote(self):
        # '(+ 1 '2) == (quote (+ 1 (quote 2)))
        tokens = ["'", '(', '+', '1', "'", '2', ')']

        ast = list(parse(tokens))
        expected = [
            [Symbol('quote'), [Symbol('+'), 1, [Symbol('quote'), 2]]]
        ]
        self.assertEqual(expected, ast)

    def test_floating_point(self):
        # 1.1 1 3.14
        tokens = ['1.1', '1', '3.14']

        ast = list(parse(tokens))
        expected = [
            1.1,
            1,
            3.14
        ]
        self.assertEqual(expected, ast)
