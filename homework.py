# Calculator app

from helper import d, fd, welcome, clear, reset, exit
from operations import addition, subtraction, division, multiply, exponents

def main():
    welcome()
    while True:
        action = input('''
Select an action you'd like to perform:

1 - Addition
2 - Subtraction
3 - Division
4 - Muliplication
5 - Exponents
6 - Quit
''')
        
        if action == "1":
            reset()
            addition() # addition function
        elif action == '2':
            reset()
            subtraction() # subtraction function
        elif action == '3':
            reset()
            division() # division
        elif action == '4':
            reset()
            multiply() # multiplication
        elif action == '5':
            reset()
            exponents() # exponents
        elif action == '6':
            clear()
            exit()
            break

main()