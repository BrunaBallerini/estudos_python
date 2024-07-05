# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type:ignore

from abc import ABC, abstractmethod


class ItemMenu(ABC):
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    @abstractmethod
    def apply_discount(self, discount):
        pass


class Dish(ItemMenu):
    def __init__(self, name, price, description) -> None:
        super().__init__(name, price)
        self.description = description

    def apply_discount(self, discount):
        self.price -= (self.price * discount)
        return self.price

    def __str__(self) -> str:
        return self.name


class Beverage(ItemMenu):
    def __init__(self, name, price, size) -> None:
        super().__init__(name, price)
        self.size = size

    def apply_discount(self, discount):
        self.price -= (self.price * discount)
        return self.price

    def __str__(self) -> str:
        return self.name
