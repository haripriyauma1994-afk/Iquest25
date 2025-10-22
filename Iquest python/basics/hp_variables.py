'''
Created on 11-Oct-2025

@author: ABC

Variables: Name given to the container in a memory location which stores data(input/output)

Data stored in the Location/container can be changed.

syntax:

variable_name = Value
                                                                        
Invalid cases:
1. while defining the variables variable name should always be in Left Hand Side and value should be in right hand Side
2. variable name should start with a character/ Letter. It should not start with numbers
3. Numerical values should not start with 0

comments: Which gives description about single line / block of a code

Types of comments:
1. Single line comments, #
2. Multi-line comments, triple-single quotes/ triple-double quotes

'''

# Defining one variable at a time--> Single line comment
num1 = 25
num2 = 34.5
num3 = 4+5j
name = "iquest"
print(num1)
print(id(num1))

#defining multiple variable in single line
num4, num5, num6 = 45, 67.8, 2+8j
print(num4)
print(id(num4))
print(num5)
print(id(num5))
print(num6)
print(id(num6))

num7 = num8 = 10
print(num7)
print(id(num7))
print(num8)
print(id(num8))

num8=20
print(num8)
print(id(num8))

num7 = num8 =10
print(num7, num8)

num4, num5, num6 = 45, 67.8, 2+8j
print("num5:", num5)