import io
import unittest

from noname import tokenize


class TestLexer(unittest.TestCase):
    def to_char_stream(self, string):
        for c in string:
            yield c

    def test_easy(self):
        source = self.to_char_stream('(+ 1 2')
        result = list(tokenize(source))
        tokens = ['(', '+', '1', '2']
        self.assertEqual(tokens, result)

    def test_simple(self):
        source = self.to_char_stream('(is-geonu? "Geonu Choi" 24 173.2 true)')
        result = list(tokenize(source))
        tokens = ['(', 'is-geonu?', '"Geonu Choi"', '24', '173.2', 'true', ')']
        self.assertEqual(tokens, result)

    def test_whitespace(self):
        source = self.to_char_stream('    (   is-geonu?"Geonu Choi" 24 173.2 \'true)')
        result = list(tokenize(source))
        tokens = ['(', 'is-geonu?', '"Geonu Choi"', '24', '173.2', "'",
                  'true', ')']
        self.assertEqual(tokens, result)

    def test_nested(self):
        source = self.to_char_stream('(defn positive? (x) (if (> x 0) true false))')
        result = list(tokenize(source))
        tokens = ['(', 'defn', 'positive?',
                  '(', 'x', ')',
                  '(', 'if', '(', '>', 'x', '0', ')', 'true', 'false', ')',
                  ')']
        self.assertEqual(tokens, result)

    def test_complex_string(self):
        expected = r'"Complex   \n-string\""'
        source = self.to_char_stream(expected)
        result = list(tokenize(source))
        self.assertEqual([expected], result)

    def test_escape_string(self):
        expected = r'"escape\\"'
        source = self.to_char_stream(expected)
        result = list(tokenize(source))
        self.assertEqual([expected], result)

    def test_stream(self):
        def to_char_stream(stream):
            for line in stream:
                for c in line:
                    yield c

        stream = io.StringIO()
        token_stream = tokenize(to_char_stream(stream))

        stream.write('(12 "foo" + 12 11 "foo" 11 ')
        stream.seek(0)

        self.assertEqual('(', next(token_stream))
        self.assertEqual('12', next(token_stream))
        self.assertEqual('"foo"', next(token_stream))
        self.assertEqual('+', next(token_stream))
        self.assertEqual('12', next(token_stream))
        self.assertEqual('11', next(token_stream))
        self.assertEqual('"foo"', next(token_stream))
        self.assertEqual('11', next(token_stream))
        try:
            next(token_stream)
        except StopIteration:
            pass
        else:
            assert False, "StopIteration not occurred"


if __name__ == '__main__':
    unittest.main()
