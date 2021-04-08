# This program takes number from user, then determine if the number is even or odd.
# Learning functions, conditional statements, and string formatting.

import sys


def init():
    print('\n' + '**' * 10 + ' NUMBER GUESS GAME ' + '**' * 10 + '\n')
    user_input = int(input('Enter a whole number: \n'))

    if (user_input % 2) == 0:
        even_number(user_input)

    elif (user_input % 2) == 1:
        odd_number(user_input)

    else:
        print('\nInvalid input! ')
        init()


def even_number(user):
    print(f'{user} is even number.\n')
    more_option()


def odd_number(user):
    print(f'{user} is odd number. \n')
    more_option()


def more_option():
    print('Do you wish to check another number? ')
    print('1. Yes \n2. No \n')
    user_choice = int(input('Select your option: \n'))

    if user_choice == 1:
        init()

    elif user_choice == 2:
        exit_user()

    else:
        print('Invalid option selected. ')
        more_option()


def exit_user():
    print('\n' + '**' * 10 + ' THANK YOU ' + '**' * 10 + '\n')
    sys.exit()


init()
