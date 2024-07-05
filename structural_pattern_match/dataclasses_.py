# pylint: disable=import-error
'''Training module for dataclasses'''


from dataclasses import dataclass, field


class OldPerson:
    '''Common class'''

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        class_str = f'{self.__class__.__name__} ' \
            f'{self.first_name} {self.last_name}'
        return class_str

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __value: object) -> bool:
        return self.first_name == __value.first_name  # type: ignore


@dataclass(frozen=True)
class Person:
    '''Dataclass'''
    first_name: str
    last_name: str
    activated: bool = False
    addresses: list = field(
        default_factory=list,
        repr=False,
        compare=False,
        kw_only=True,
    )
    full_name: str = field(default='Missing', init=False)

    def __post_init__(self):
        full_name = f'{self.first_name} {self.last_name}'
        object.__setattr__(
            self,
            'full_name', full_name
        )


if __name__ == '__main__':
    john = Person('John', 'Doe', True, addresses=['Rua 1'])
    print(john)
    john_2 = Person('John', 'Doe', True, addresses=['Rua 2'])
    mary = Person('Mary', 'Jane')
    print(repr(mary))
    print(john == john_2)
    # john.activated = True
    print(john)
