'''Module for unittest'''
import unittest

from calc import sum_


class TestCalc(unittest.TestCase):
    '''Class for tests related to module calc.py'''

    def test_sums_of_five_and_five_returns_ten(self):
        '''Test for sums of five and five returns ten '''
        self.assertEqual(sum_(5, 5), 10)

    def test_sums_of_five_and_fourteen_returns_ten(self):
        '''Test for sums of five and fourteen returns ten '''
        self.assertEqual(sum_(5, 14), 19)

    def test_varios(self):
        '''Test for sums of multiple values '''
        x_y_results = (
            (-5, 5, 0),
            (1.5, 1.5, 3.0),
            (10, 20, 30),
        )

        for x_y_result in x_y_results:
            with self.subTest(x_y_result=x_y_result):
                x, y, result = x_y_result
                self.assertEqual(sum_(x, y), result)

    def test_x_is_not_int_or_float_return_assertion_error(self):
        '''Error return test case x is string'''
        with self.assertRaises(AssertionError):
            sum_('a', 10)

    def test_y_is_not_int_or_float_return_assertion_error(self):
        '''Error return test case y is string'''
        with self.assertRaises(AssertionError):
            sum_(10, 'b')


if __name__ == '__main__':
    unittest.main(verbosity=2)  # type: ignore
