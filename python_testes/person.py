'''Module person.py'''
import requests  # pylint: disable=import-error


class Person:
    '''Class created for tests TDD'''

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.data = False

    def get_data(self):
        '''API simulation'''
        response = requests.get(
            'https://docs.python.org/3/library/unittest.html')

        if response.ok:
            self.data = True
            return 'Connected'
        self.data = False
        return '404 error'
