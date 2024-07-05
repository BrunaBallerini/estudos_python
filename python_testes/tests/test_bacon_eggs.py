'''
TDD - Test driven development -> Red - Green - Refactor
'''

import unittest

from bacon_eggs import bacon_with_eggs


class TestBaconWithEggs(unittest.TestCase):
    '''Tests for mudule bacon_eggs.py'''

    def test_bacon_with_eggs_raises_assertion_error_if_not_receive_int(self):
        '''Tests module raises assertion error if it does not receive int'''
        with self.assertRaises(AssertionError):
            bacon_with_eggs('a')

    def test_x_is_multiple_of_3_and_5_returns_bacon_with_eggs(self):
        '''X is multiple of 3 and 5'''
        values = (15, 30, 45, 60)
        output = 'bacon with eggs'

        for value in values:
            with self.subTest(value=value, output=output):
                self.assertEqual(
                    bacon_with_eggs(value),
                    output
                )

    def test_x_is_not_multiple_of_3_and_5_returns_nothing_to_eat(self):
        '''X is not multiple of 3 and 5'''
        values = (1, 2, 4, 7, 8)
        output = 'nothing to eat'

        for value in values:
            with self.subTest(value=value, output=output):
                self.assertEqual(
                    bacon_with_eggs(value),
                    output
                )

    def test_x_is_multiple_of_3_returns_bacon(self):
        '''X is multiple of 3'''
        values = (3, 6, 9, 12)
        output = 'bacon'

        for value in values:
            with self.subTest(value=value, output=output):
                self.assertEqual(
                    bacon_with_eggs(value),
                    output
                )

    def test_x_is_multiple_of_5_returns_eggs(self):
        '''X is multiple of 5'''
        values = (5, 10, 20, 25)
        output = 'eggs'

        for value in values:
            with self.subTest(value=value, output=output):
                self.assertEqual(
                    bacon_with_eggs(value),
                    output
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)  # type: ignore
