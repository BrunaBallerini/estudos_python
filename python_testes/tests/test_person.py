'''
class Person:
    __ini__
        first_name str
        last_name str
        data bool False

    API:
    get_data -> method
        OK
        404

'''

import unittest
from unittest.mock import patch

from person import Person


class TestPerson(unittest.TestCase):
    '''Class for tests related to module person.py'''

    def setUp(self):
        self.p1 = Person('Bruna', 'Ballerini')
        self.p2 = Person('Maria', 'Miranda')

    def test_persons_firts_name_is_correct(self):
        '''Checks persons first name is correct'''
        self.assertEqual(self.p1.first_name, 'Bruna')
        self.assertEqual(self.p2.first_name, 'Maria')

    def test_persons_first_name_is_str(self):
        '''Checks persons first name is string'''
        self.assertIsInstance(self.p1.first_name, str)
        self.assertIsInstance(self.p2.first_name, str)

    def test_persons_last_name_is_correct(self):
        '''Checks persons last name is correct'''
        self.assertEqual(self.p1.last_name, 'Ballerini')
        self.assertEqual(self.p2.last_name, 'Miranda')

    def test_persons_last_name_is_str(self):
        '''Checks persons last name is string'''
        self.assertIsInstance(self.p1.last_name, str)
        self.assertIsInstance(self.p2.last_name, str)

    def test_persons_data_inicialize_as_false(self):
        '''Checks that person instance has data=False'''
        self.assertFalse(self.p1.data)
        self.assertFalse(self.p2.data)

    def test_data_successfully_connected_ok(self):
        '''Checks that data successfully connected OK'''
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.p1.get_data(), 'Connected')
            self.assertTrue(self.p1.data)
            self.assertEqual(self.p2.get_data(), 'Connected')
            self.assertTrue(self.p2.data)

    def test_data_unsuccessfully_connected_fail(self):
        '''Checks that the connection fail'''
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            self.assertEqual(self.p1.get_data(), '404 error')
            self.assertFalse(self.p1.data)
            self.assertEqual(self.p2.get_data(), '404 error')
            self.assertFalse(self.p2.data)

    def test_data_connected_and_fail_sequential(self):
        '''Checks that the connection was successfull and fail in sequence'''
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.p1.get_data(), 'Connected')
            self.assertTrue(self.p1.data)
            self.assertEqual(self.p2.get_data(), 'Connected')
            self.assertTrue(self.p2.data)

            fake_request.return_value.ok = False
            self.assertEqual(self.p1.get_data(), '404 error')
            self.assertFalse(self.p1.data)
            self.assertEqual(self.p2.get_data(), '404 error')
            self.assertFalse(self.p2.data)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # type: ignore
