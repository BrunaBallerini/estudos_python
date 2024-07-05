# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-name-in-module
# pylint: disable=import-error
# type:ignore

from methods.avaliacao import Avaliacao
from methods.menu import ItemMenu


class Restaurant:
    restaurants: list[object] = []

    def __init__(self, name: str, category: str) -> None:
        self.name = name.capitalize()
        self.category = category
        self._status = False
        self._notes = []
        self.menu = []
        Restaurant.restaurants.append(self)

    @property
    def status(self):
        return 'Ativo' if self._status else 'Inativo'

    @status.setter
    def status(self, value):
        self._status = value

    def __repr__(self) -> str:
        return f'{self.name} | {self.category}'

    @classmethod
    def list_restaurants(cls):
        print(f'{"Restaurant".ljust(25)} | {"Category".ljust(25)} | '
              f'{"Status".ljust(25)} | {"Note"}')
        for restaurant in Restaurant.restaurants:
            print(f'{restaurant.name.ljust(25)} | '
                  f'{restaurant.category.ljust(25)} | '
                  f'{restaurant.status.ljust(25)} | '
                  f'{restaurant.media_avaliation}')

    def change_status(self):
        self._status = not self._status

    def receive_avaliation(self, cliente, nota):
        if nota > 6:
            nota = 5
        avaliacao = Avaliacao(cliente, nota)
        self._notes.append(avaliacao)

    @property
    def media_avaliation(self):
        if not self._notes:
            return '-'
        sum_notes = sum(avaliacao.nota for avaliacao in self._notes)
        amount_notes = len(self._notes)
        media = round(sum_notes / amount_notes, 1)
        return media

    def add_on_menu(self, thing_to_add):
        if isinstance(thing_to_add, ItemMenu):
            self.menu.append(thing_to_add)

    def show_menu(self):
        print(f'Menu of {self.name}:')
        for i, item_ in enumerate(self.menu, start=1):
            if hasattr(item_, 'description'):
                message_dish = (f'{i} - Name: {item_.name} | '
                                f'Price: {item_.price} | '
                                f'Description: {item_.description}')
                print(message_dish)
            elif hasattr(item_, 'size'):
                message_beverage = (f'{i} - Name: {item_.name} | '
                                    f'Price: {item_.price} | '
                                    f'Size: {item_.size}')
                print(message_beverage)
