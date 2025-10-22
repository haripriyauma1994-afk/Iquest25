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

print("==========converting float to other data type==========")

num9 = int(num2)
print('num9 :', num9)
print("type of num9: ", type(num9))

num10 = complex(num2)
print('num10: ', num10)
print("type of num10: ", type(num10))

num11 = str(num2)
print('num11: ', num11)
print("type of num11: ", type(num11))

num12 = bool(num2)
print('num12: ', num12)
print("type of num12: ", type(num12))

print("============converting complex to other data type============")

# num13 = int(num3)- TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

# num14 = float(num3) - TypeError: float() argument must be a string or a real number, not 'complex'

num15 = str(num3)
print('num15:',num15)
print("type of num15: ", type(num15))

num16 = bool(num3)
print('num16:',num16)
print("type of num16: ", type(num16))

print('=============converting string to other data types===============')
'''
#name1 = int(name) ValueError: invalid literal for int() with base 10: 'Vivek'
name2 = float(name) ValueError: invalid literal for int() with base 10: 'Vivek'

If you actually want to convert numeric input, make sure the string contains digits:

Ex: name = "123"
name1 = int(name)
'''
name3 = bool(name)
print('name3:',name3)
print(type(name3))

print("=============converting boolean to other data type=============")

var4 = int(var1)
print('var4: ',var4)
print("type of var4: ",type(var4))

var5 = float(var1)
print('var5:',var5)
print(type(var5))

var6 = complex(var1)
print('var6:',var6)
print(type(var6))

var7 = str(var1)
print('var7:',var7)
print(type(var7))

