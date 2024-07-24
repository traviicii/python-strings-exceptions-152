from helper import d

# In Python there are only two types of issues that will break your code
#-- stop your code from functioning or executing, and throw an error

# Syntax Errors : error in your coding grammar, a structural error
# ---- misspelling
# --- indentation error
# --- code structure is missing something
# --- colons, indentation, parenthesis, ' ', " "

# Exceptions : arise when our code is structured correctly, but some operation doesn't execute for a variety of reasons

#--- ZeroDivisionError : occurs when you try to divide by 0
quotient = 10/0

#--- NameError : trying to call a variable or function before it's defined
print(x)
print(divi())
def divi():
    pass

#--- ValueError : trying perform operations with invalid values

str_num = 'nine'
int_num = int(str_num) # trying to convert an invalid value

#--- TypeError : trying to perform operations on values of inappropriate types

num = 5
total_people = num + "people" # cannot concatenate a str and an int together

#--- AttributeError : trying to use methods on improper objects

word = "Hello"
word.append("World")

rword = word.reversed()
