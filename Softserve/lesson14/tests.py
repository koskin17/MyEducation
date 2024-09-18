import unittest

from funk import cout_chen, quadratic_expression

class CoutChenTests(unittest.TestCase):

    def test_1(self):
        actual = cout_chen("hello")
        expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        self.assertEqual(actual, expected)
    def test_2(self):
        actual = cout_chen("hello")
        expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        self.assertIn('h', actual)
    def test_3(self):
        actual = cout_chen("hello")
        expected = {'h': 1, 'e': 4, 'l': 2, 'f': 1}
        self.assertEqual(actual, expected)
    def test_quadratic_expression_1(self):
        actual = quadratic_expression(1,3,1)
        expected = (-2.618033988749895, -0.3819660112501051)
        self.assertEqual(actual, expected)
    def test_quadratic_expression_2(self):
        actual = quadratic_expression(1,4,1)
        expected = (-3.732050807568877, -0.3819660112501051)
        self.assertEqual(actual, expected)
    def test_quadratic_expression_3(self):
        actual = quadratic_expression(1,2,3)
        
        self.assertIsNone(actual)
    def test_quadratic_expression_4(self):
        actual = quadratic_expression(1,2,1)
        expected = -1
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()