'''Main module'''

from calc import sum_


def main():
    '''Função main'''
    try:
        result = sum_('15', 15)
        print(result)
    except AssertionError as e:
        print(f'Invalid number: {e}')

    result2 = sum_(15, 15)
    print(result2)


if __name__ == '__main__':
    main()
