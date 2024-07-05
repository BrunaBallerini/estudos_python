# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# type:ignore

from menu.item_menu import ItemMenu


class Dish(ItemMenu):
    def __init__(self, name, price, description) -> None:
        super().__init__(name, price)
        self.description = description
