import unittest
import calc


class TestShape(unittest.TestCase):

    def test___add__(self):
        shape1 = calc.Shape((1, 2), (2, 2), (2, 3))
        shape2 = calc.Shape((2, 2), (3, 4), (4, 5))
        self.assertEqual(shape1 + (3, 1), [(4, 3), (5, 3), (5, 4)])
        self.assertEqual(shape2 + (-4, 100), [(-2, 102), (-1, 104), (0, 105)])
        self.assertEqual(shape1 + (1, -10), [(2, -8), (3, -8), (3, -7)])


if __name__ == '__main__':
    unittest.main()
