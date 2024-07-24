
def addition():
    '''Get inputs a and b from the user and add them together.'''
    while True:
        try:
            a = int(input("Please enter the first number for the addition operation: "))
            b = int(input("Please enter the second number: "))
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of adding {a} + {b} = {a + b}")
            break

def subtraction():
    '''Get inputs a and b from the user and subtract.'''
    while True:
        try:
            a = float(input("Please enter the first number for the subtraction operation: "))
            b = float(input("Please enter the second number: "))
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of subtracting {a} - {b} = {a - b}")
            break

def division():
    '''Get inputs a and b from the user and divides them.'''
    while True:
        try:
            a = float(input("Please enter the first number for the division operation: "))
            b = float(input("Please enter the second number: "))
            ans = a/b
        except ValueError:
            print("Please enter valid numbers!")
        except ZeroDivisionError:
            print("Yooooo you can't divide by zero fool!!!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of dividing {a} / {b} = {round(ans, 2)}")
            break

def multiply():
    '''Get inputs a and b from the user and multiplies them.'''
    while True:
        try:
            a = float(input("Please enter the first number for the multiplication operation: "))
            b = float(input("Please enter the second number: "))
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of multiplying {a} x {b} = {a * b}")
            break