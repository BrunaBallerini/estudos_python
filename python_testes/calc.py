'''Module with the sum function'''


def sum_(x, y):
    '''Função que calcula somatório de dois numeros
    >>> sum_(10, 20)
    30
    >>> sum_(15, 25)
    40
    >>> sum_('15', 10)
    Traceback (most recent call last):
    ...
    AssertionError: X need to be int or float
    '''
    assert isinstance(x, (float, int)), 'X need to be int or float'
    assert isinstance(y, (float, int)), 'Y need to be int or float'
    return x + y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
