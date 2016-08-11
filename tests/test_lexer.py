import unittest

from noname import tokenize


class TestLexer(unittest.TestCase):
    def test_easy(self):
        source = '(+ 1 2'
        result = tokenize(source)
        tokens = ['(', '+', '1', '2']
        self.assertEqual(tokens, result)

    def test_simple(self):
        source = '(is-geonu? "Geonu Choi" 24 173.2 true)'
        result = tokenize(source)
        tokens = ['(', 'is-geonu?', '"Geonu Choi"', '24', '173.2', 'true', ')']
        self.assertEqual(tokens, result)

    def test_whitespace(self):
        source = '    (   is-geonu?"Geonu Choi" 24 173.2 \'true)'
        result = tokenize(source)
        tokens = ['(', 'is-geonu?', '"Geonu Choi"', '24', '173.2', "'",
                  'true', ')']
        self.assertEqual(tokens, result)

    def test_nested(self):
        source = '(defn positive? (x) (if (> x 0) true false))'
        result = tokenize(source)
        tokens = ['(', 'defn', 'positive?',
                  '(', 'x', ')',
                  '(', 'if', '(', '>', 'x', '0', ')', 'true', 'false', ')',
                  ')']
        self.assertEqual(tokens, result)

    def test_complex_string(self):
        source = r'"Complex   \n-string\""'
        result = tokenize(source)
        self.assertEqual([source], result)


if __name__ == '__main__':
    unittest.main()
