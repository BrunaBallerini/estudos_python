# pylint: disable=invalid-name

"""
Testing type annotations in module with python 3.10.
https://docs.python.org/3/library/typing.html
"""

from collections.abc import Callable
from typing import Sequence, TypeVar

var_string: str = 'string'
var_int: int = 45
var_float: float = 2.2
var_bool: bool = True
var_set: set = {1, 2, 3}
var_list: list[int | str] = [1, 2, 3, 'bruna']
var_tuple: tuple[int, int, int, str] = (1, 2, 3, 'bruna')
var_dict: dict[str, list[int]] = {'key': [1, 2]}
var_dict_: dict[str, str | int | list[int]] = {
    'nome': 'bruna', 'sobrenome': 'ballerini', 'idade': 35,  'lista': [1, 2]}


def soma(x: int, y: int, z: int) -> float:
    """Testing type annotations in function with python 3.10."""
    return x + y + z


IntegerList = list[int]  # Type Alias
DictIntegerList = dict[str, IntegerList]

var_str_int: str | int = 1
var_str_int = 'a'
print(var_str_int)

var_list2: list[int | str] = [1, 'a', 3]


def soma2(x: int, y: float | None) -> float:
    """Testing type annotations in function with python 3.10."""
    if isinstance(y, float | int):
        return x + y
    return x + x


T = TypeVar('T')

SomaInteiros = Callable[[int, int], int]


def executa(func: SomaInteiros, x: int, y: int) -> int:
    """Testing type annotations in function with python 3.10."""
    return func(x, y)


def return_function(function: Callable[[], None]) -> Callable:
    '''
    Function that returns another function
    Callable[receive nothing in the parameters, returns None]
    '''
    return function


def says_hi():
    '''Function print hi in the console'''
    print('hi')


return_function(says_hi)()


def return_function_(function: Callable[[int, int], int]) -> Callable:
    '''
    Function that returns another function
    Callable[receive nothing in the parameters, returns None]
    '''
    return function


def sum_(x: int, y: int) -> int:
    '''Function print hi in the console'''
    return x + y


print(return_function_(sum_)(1, 2))


class Person:
    '''Class created for learning type annotations'''

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.firt_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age

    def __str__(self) -> str:
        return f'{self.firt_name} {self.last_name}'


def iteration(sequence: Sequence[int]):
    '''Iteration function'''
    return [x * 2 for x in sequence]


# list_for_iteration: list[int] = [x for x in range(1, 11)]
list_for_iteration: list[int] = list(range(1, 11))
print(iteration(list_for_iteration))
