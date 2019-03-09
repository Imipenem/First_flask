import unittest


class SimpleTest(unittest.TestCase):

    def test_fun(self):
        self.assertEqual(100, 10*10)

if __name__ == '__main__':
    unittest.main()