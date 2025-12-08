'''
Created on 06-Nov-2025

@author: ABC
Function: A block of code with a specific name to perform certain tasks

A function can be called by using the name with paranthesis.
A function can take user input with the help of parameters(variables defined within paranthesis).
Defining Parameters are optional based upon the requirement

def function_name(a, b): -->defining the function

Mandatory --> def, function_name, (), :
Optional --> a, b

function_name() --> calling

Types of functions:
1. Predefined functions
    - built-in functions
    Ex: print(), id(), input()...

2. User-defined functions

Advantage:

1. It reduces code repetition/ increases code re-usability
2. Easy maintenance of code 


'''
'''
a=6
b=8
c=a+b
print(f"Sum of {a} and {b} is", a+b)
print("=======Addition Completed========")

a=6
b=8
c=a+b
print(f"Sum of {a} and {b} is", a+b)
print("=======Addition Completed========")

a=6
b=8
c=a+b
print(f"Sum of {a} and {b} is", a+b)
print("=======Addition Completed========")
'''

def welcome(): # Function without parameters
    print("Welcome to iQuest!!")
    
def add(a, b): # Function with parameters
    # print("=======Addition Started========")
    c=a+b
    # print(f"Sum of {a} and {b} is", c)
    # print("=======Addition Completed========")
    return c # returns value when function is called. return statement is optional

def sub(a, b):
    c=a-b
    return c

def add_sub(a, b):
    c = add(a, b) # calling a function inside another function
    d = sub(a, b)
    return c, d # returning multiple values

welcome()
add(3, 4)
add(2, 6)
result = add(7, 9)
print("result-->", result)
x, y = add_sub(38, 25) # Unpacking of tuple
print("Result of add_sub():", x, y)

addition = add # Creating alias/ assigning a function to a variable
print(addition(4, 7)) # passing a function as parameter to another function

