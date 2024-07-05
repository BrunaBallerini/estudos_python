# pylint: disable=missing-module-docstring
# pylint: disable=E0611:no-name-in-module
# type:ignore

from methods.menu import Beverage, Dish
from methods.restaurant import Restaurant

if __name__ == '__main__':

    pizza = Restaurant('Pizza na Roça', 'Pizzaria')
    # print(pizza)
    # print(dir(pizza))
    shushi = Restaurant('Rioshy', 'Japones')
    pizza.receive_avaliation('Gui', 10)
    pizza.receive_avaliation('Lais', 8)
    pizza.receive_avaliation('Emy', 5)
    shushi.receive_avaliation('Gui', 10)
    shushi.receive_avaliation('Lais', 8)
    shushi.receive_avaliation('Emy', 2)
    beverage_juice = Beverage('Orange juice', 18, 500)
    dish_bread = Dish('Bread', 1.25, 'The best in town.')
    # print(beverage_juice)
    # print(dish_bread)
    pizza.add_on_menu(beverage_juice)
    pizza.add_on_menu(dish_bread)
    pizza.change_status()
    Restaurant.list_restaurants()
    print()
    pizza.show_menu()
    print()
    beverage_juice.apply_discount(0.08)
    dish_bread.apply_discount(0.05)
    pizza.show_menu()
