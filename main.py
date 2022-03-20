import art
print(art.logo)

import os

# Importing our main calculator!
from Calc import *

# Making a calculator class
my_calculator = Calculator()

while True:

    print('1: ADDITION\n2: SUBTRACTION\n3: MULTIPLICATION\n4: DIVISION\n5: FACTORIAL\n6: SQUARE\n7: SQUARE-ROOT\n0: EXIT')
    choice = input('\nEnter your choice: ')
    
    # Exit calculator
    if choice == '0':
        break

    # Making sure user choice is correct
    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        
        # SINGLE NUMBER CALCULATION!
        if choice in ['5', '6', '7']:
            num_1 = int(input('\nEnter number: '))
            num_2 = None
            
        # DUAL NUMBER CALCULATIONS!
        else:
            num_1 = int(input('\nEnter first number: '))
            num_2 = int(input('Enter second number: '))
        
        # Zero-Division!
        while num_2 == 0 and choice == '4':
            num_2 = int(input('Sorry! Can not divide by zero, please enter again: '))
            
    else:
        print('\nInvalid input, please enter again')
        # os.system('cls')
        continue

    # Calculating the result!
    print()
    if choice == '1':
        ans = my_calculator.give_sum(num_1,num_2)
        print(f'{num_1} + {num_2} = {ans}')
    elif choice == '2':
        ans = my_calculator.give_sub(num_1,num_2)
        print(f'{num_1} - {num_2} = {ans}')
    elif choice == '3':
        ans = my_calculator.give_product(num_1,num_2)
        print(f'{num_1} x {num_2} = {ans}')
    elif choice == '4':
        ans = my_calculator.give_div(num_1,num_2)
        print(f'{num_1} / {num_2} = {ans}')
    elif choice == '5':
        ans = my_calculator.give_fact(num_1)
        print(f'{num_1}! = {ans}')
    elif choice == '6':
        ans = my_calculator.give_square(num_1)
        print(f'{num_1}^2 = {ans}')
    elif choice == '7':
        ans = my_calculator.give_squareroot(num_1)
        print(f'{num_1}^1/2 = {ans}')
        
    # If want to calculate again!
    again = input('\nWant to calculate again(Y/N): ')
    
    if again[0].upper() == 'Y':
        os.system('cls')
        print(art.logo)
        continue
    elif again[0].upper() == 'N':
        print(f'\nThanks for calculating with us!')
        break
    else:
        print('\nInvalid input, exiting program!')
        break