import unittest

from noname import Symbol, Environment


class TestEnvironment(unittest.TestCase):
    def test_easy(self):
        env = Environment(None)
        env.set(Symbol('a'), 1)
        self.assertEqual(1, env.find(Symbol('a')))
        self.assertRaises(NameError, env.find, Symbol('b'))
        env.set(Symbol('b'), 2)
        self.assertEqual(2, env.find(Symbol('b')))

    def test_parent(self):
        root = Environment(None)
        root.set(Symbol('a'), 1)
        env = Environment(root)
        env.set(Symbol('b'), 2)
        self.assertEqual(2, env.find(Symbol('b')))
        self.assertEqual(1, env.find(Symbol('a')))

    def test_overwrite(self):
        root = Environment(None)
        root.set(Symbol('a'), 1)
        env = Environment(root)
        env.set(Symbol('a'), 2)
        self.assertEqual(2, env.find(Symbol('a')))
        self.assertEqual(1, root.find(Symbol('a')))


if __name__ == '__main__':
    unittest.main()
