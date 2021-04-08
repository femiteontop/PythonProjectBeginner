# This program will solve basic mathematics equations.

import math
import sys


def init():
    print('\n' + '++' * 10 + ' MATHEMATICAL EQUATIONS ' + '++' * 10 + '\n')
    print('Which Mathematical equation do you wish to solve? ')
    print('1. Quadratic Equation: ')
    print('2. Pythagoras Equation: ')
    print('3. Volume of Cylinder: ')
    print('4. Area of Rectangle: ')
    print('5. Simple Interest: \n')
    selected_option = int(input('Select an option: \n'))

    if selected_option == 1:
        quadratic_equation()

    elif selected_option == 2:
        pythagoras_theorem()

    elif selected_option == 3:
        cylinder_volume()

    elif selected_option == 4:
        rectangle_area()

    elif selected_option == 5:
        simple_interest()

    else:
        print('Invalid option selected, try again...')
        init()


def quadratic_equation():
    print('To calculate Quadratic Equation, for ax2 + bx + c = 0, use x = (-b±√(b^2-4ac))/2a:  ')
    a = float(input('Enter co-efficient of x2: \n'))
    b = float(input('Enter co-efficient of x: \n'))
    c = float(input('Enter constant value: \n'))

    x1 = -b + (math.sqrt((math.pow(b, 2) - (4 * a * c))) / (2 * a))
    x2 = -b - (math.sqrt((math.pow(b, 2) - (4 * a * c))) / (2 * a))

    print(f"The roots of the equation are {x1} and {x2}")
    more_try()


def pythagoras_theorem():
    print('To calculate Pythagoras Equation, use hyp = √opp2 + adj2')
    opp = float(input('Enter opposite value: \n'))
    adj = float(input('Enter adjacent value: \n'))

    hyp = math.sqrt(math.pow(opp, 2) + math.pow(adj, 2))

    print(f'The value of hypotenuse is {hyp}')
    more_try()


def cylinder_volume():
    print("To calculate Volume of a Cylinder, use v = πr²h: ")
    cylinder_radius = float(input('Enter value of radius, r: \n'))
    cylinder_height = float(input('Enter value of height, h: \n'))

    volume = "{:.2f}".format(math.pi * math.pow(cylinder_radius, 2) * cylinder_height)

    print(f'The volume of cylinder is {volume}')
    more_try()


def rectangle_area():
    print('To calculate Area of Rectangle, use A = L * B: ')
    rectangle_length = float(input('Enter length of rectangle: \n'))
    rectangle_breadth = float(input('Enter breadth of rectangle: \n'))
    area = rectangle_length * rectangle_breadth

    print(f'The Area of Rectangle is {area}')
    more_try()


def simple_interest():
    print('To calculate Simple Interest, use I = PRT/100: ')
    s_principal = float(input('Enter Principal value: \n'))
    s_rate = float(input('Enter Rate value: \n'))
    s_time = float(input('Enter time value in years: \n'))

    s_interest = (s_principal * s_rate * s_time) / 100
    print(f'The Simple Interest is {s_interest}')
    more_try()


def more_try():
    print('\nDo you wish to try another equation? ')
    print('1. Yes \n2. No ')
    user_choice = int(input('Select your option: \n'))

    if user_choice == 1:
        init()

    elif user_choice == 2:
        exit_user()

    else:
        print('Invalid option selected, try again...')
        more_try()


def exit_user():
    print('\n' + '++' * 10 + ' THANK YOU ' + '++' * 10 + '\n')
    sys.exit()


init()
