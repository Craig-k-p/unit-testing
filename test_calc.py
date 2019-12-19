import unittest
import calc
from unittest.mock import patch


class TestShape(unittest.TestCase):

    @classmethod
    def setUp(self):
        print('setUp class method')

    @classmethod
    def tearDown(self):
        print('tearDown class method')

    def setUp(self):
        self.shape1 = calc.Shape((1, 2), (2, 2), (2, 3))
        self.shape2 = calc.Shape((2, 2), (3, 4), (4, 5))

    def tearDown(self):
        del self.shape1
        del self.shape2

    def test___add__(self):
        self.assertEqual(self.shape1 + (3, 1), [(4, 3), (5, 3), (5, 4)])
        self.assertEqual(self.shape2 + (-4, 100), [(-2, 102), (-1, 104), (0, 105)])
        self.assertEqual(self.shape1 + (1, -10), [(2, -8), (3, -8), (3, -7)])

        self.assertRaises(ValueError, self.shape1.__add__, 'oops')
        self.assertRaises(ValueError, self.shape1.__add__, 5)
        # self.assertRaises(ValueError, self.shape1.__add__, (1, 2)) # raises ValueError

        with self.assertRaises(ValueError):
            self.shape2 + 'a'
            self.shape2 + 4
            self.shape2 + [5, 2]

    def test_move(self):
        '''Mock return values for methods that might fail, such as requests to a server that is down. 
        '''
        with patch('Shape.transform') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'


if __name__ == '__main__':
    unittest.main()
