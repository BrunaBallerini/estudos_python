# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import os

restaurants = [{'name': 'Ryosh', 'category': 'Japanese', 'status': False}]
# restaurants = [dict()]


def show_options():
    print('Express Flavor')
    print('1. Register Restaurant')
    print('2. List Restaurant')
    print('3. Activate Restaurant')
    print('4. Quit\n')


def main_menu():
    show_options()
    try:
        chosen_option = int(input('Chose the option: '))
        print(f'Option: {chosen_option}')
        if chosen_option == 1:
            register_restaurant()
        elif chosen_option == 2:
            list_restaurant()
        elif chosen_option == 3:
            activate_restaurant()
        elif chosen_option == 4:
            quit_()
        else:
            invalid_option()
    except ValueError:
        invalid_option()


def return_main_menu():
    input('\nType any key to return.\n')
    main_menu()


def option_message(msg):
    os.system('clear')
    print(msg)


def register_restaurant():

    option_message('Register Restaurant')

    restaurant_name = input('Type the name of the restaurant: ')
    restaurant_category = input('Type the category of the restaurant: ')
    restaurants.append({'name': restaurant_name,
                        'category': restaurant_category,
                        'status': False
                        })
    print(f'\nThe restaurant {restaurant_name} was registered.')

    return_main_menu()


def list_restaurant():
    option_message('List Restaurant')

    print(f"{'Restaurant'.ljust(10)} | {'Category'.ljust(10)} | Status")

    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        restaurant_category = restaurant['category']
        restaurant_status = restaurant['status']
        print(
            f"{restaurant_name.ljust(10)} | "
            f"{restaurant_category.ljust(10)} | "
            f"{restaurant_status}")

    return_main_menu()


def activate_restaurant():
    option_message('Activate Restaurant')
    restaurant_for_change = input(
        'Type the restaurant that you want to change the status: ')
    restaurant_found = False

    for restaurant in restaurants:
        if restaurant_for_change == restaurant['name']:
            restaurant_found = True
            restaurant['status'] = not restaurant['status']
            print(f"\nThe restaurant {restaurant['name']} "
                  f"change the status for {restaurant['status']}.")

    if not restaurant_found:
        print('Restaurant not found.')

    return_main_menu()


def quit_():
    option_message('Quit.')


def invalid_option():
    option_message('Invalid option.')
    return_main_menu()


if __name__ == '__main__':
    main_menu()
