'''
Created on 06-Nov-2025

@author: ABC
Argument: A variable defined in function definition and values passed when a function is called
            are called as arguments

1. Formal arguments: A variable defined in function definition
2. Actual arguments: values passed when a function is called

Ex:
def add(a, b): 
    c=a+b
    return c
    
add(1, 4)

a, b --> Formal arguments
1, 4 --> Actual arguments

Types of arguments:

- Actual arguments
    1. Positional arguments 
        - actual arguments are assigned to formal arguments based on their positions
    2. Keyword arguments
        - we use formal arguments as keys to send values to the function
    
- Formal arguments:
    1. default arguments
        - we set a default value while formal arguments are defined
    2. variable length arguments
    3. Keyword variable length arguments
'''
def add(a=0, b=0): 
    c=a+b
    print(f"Sum of {a} and {b} is", c)

add(4, 5) # Positional arguments
add(6, 4)
add(b=10, a=20) # keyword arguments
add()
add(4)
# add(5, 7, 9) # TypeError: add() takes from 0 to 2 positional arguments but 3 were given

def var_len(*a): # variable length arguments
    print(a)
    
var_len(5, 7, 9)
# var_len(a=5, b=6, c=8, d=9)

def kw_var_len(**a):
    print(a)

kw_var_len(a=5, b=6, c=8, d=9)

