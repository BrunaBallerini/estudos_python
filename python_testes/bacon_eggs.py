'''
1 - int
2 - if number is multiple of 3 and 5
    return bacon and eggs
3 - if number is multiple of 3
    return bacon
4 - if number is multiple of 5
    return eggs
5 - if number is not multiple of 3 and 5
    return nothing to eat
'''


def bacon_with_eggs(x):
    '''
    Function returns some phrases depends of the x is or is not multiple
    of 3, 5 or both
    '''
    assert isinstance(x, int), 'X must be number int'
    multiple_5 = x % 5 == 0
    multiple_3 = x % 3 == 0
    if multiple_3 and multiple_5:
        return 'bacon with eggs'
    if multiple_3:
        return 'bacon'
    if multiple_5:
        return 'eggs'
    return 'nothing to eat'
