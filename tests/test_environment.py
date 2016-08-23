import unittest

from noname import Environment


class TestEnvironment(unittest.TestCase):
    def test_easy(self):
        env = Environment(None)
        env.set('a', 1)
        self.assertEqual(1, env.find('a'))
        self.assertRaises(NameError, env.find, 'b')
        env.set('b', 2)
        self.assertEqual(2, env.find('b'))

    def test_parent(self):
        root = Environment(None)
        root.set('a', 1)
        env = Environment(root)
        env.set('b', 2)
        self.assertEqual(2, env.find('b'))
        self.assertEqual(1, env.find('a'))

    def test_overwrite(self):
        root = Environment(None)
        root.set('a', 1)
        env = Environment(root)
        env.set('a', 2)
        self.assertEqual(2, env.find('a'))
        self.assertEqual(1, root.find('a'))


if __name__ == '__main__':
    unittest.main()
