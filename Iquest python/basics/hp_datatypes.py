'''

DATA TYPES


@author: Vivek

Data Types: 

type() --> Pre-defined function to determine the type of data stored in variables

Buit-in data types in Python:

Fundamental data types:
    1. Numerical data types:
        - int
        - float
        - complex
    2. String - str
    3. Boolean - True or False
    4. None
    5. Bytes
    6. Bytearray

Derived data-types/ Data-structures:
    1. List
    2. Tuple
    3. Set
    4. Dictionary
    
Type casting: Conversion of one data-type to another data-type.

This can be achieved using the built-in functions:
1. int() - converts one data-type to integer data-type
2. float() - converts to float data-type
3. complex() - converts to complex data-type
4. bool - converts to boolean data-type
5. str() - converts to string data-type

'''
num1 = 23 # int
num2 = 34.5 # float
num3 = 4+5j # complex
name = 'Vivek' # str
var1 = True # bool
var2 = False # bool
var3 = None # NoneType

print("Type of num1: ",type(num1))
print("Type of num2: ",type(num2))
print("Type of num3: ",type(num3))
print("Type of name: ",type(name))
print("Type of var1: ",type(var1))
print("Type of var2: ",type(var2))
print("Type of var3: ",type(var3))

print('=======Converting int to other data-types=======')
print('num1:', num1) 

num4 = float(num1)
print('num4:', num4)
print("Type of num4: ",type(num4))

num5 = complex(num1)
print('num5:', num5)
print("Type of num5: ",type(num5))

'''
num6 = str(num1)
print('num6:', num6)
print("Type of num6: ",type(num6)) # 
'''
num8 = -7
num7 = bool(num8)
print('num7:', num7)
print("Type of num7: ",type(num7))
