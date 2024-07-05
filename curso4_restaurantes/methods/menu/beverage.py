# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# type:ignore

from item_menu import ItemMenu


class Beverage(ItemMenu):
    def __init__(self, name, price, size) -> None:
        super().__init__(name, price)
        self.size = size
