'''
Created on 16-Oct-2025

@author: haripriya

Conditional statements: Flow of program execution will be decided based on a condition.
(Decision making statements)

Indentation: It is the leading space to define a block of code
1 indentation = 1 tab space = 4 normal 

1. if statement
2. if-else statement
3. Series if-else statements
4. nested if statements 
'''
'''
age = int(input("Please enter your age: "))

if age>12:
    print("Age is satisfied")
else:
    print("Age is not satisfied")
    
print("Program terminated")
'''

age = int(input("Please enter your age:"))

if age>0:
    if age <=3:
        print("You're a toddler")
    elif age<=12:
        print("you're a child")
    elif age<=18:
        print("you're a teenager")
    elif age<=60:
        print("you're an adult")
    else:
        print("You're senior citizen")  
else:
    print("Please enter positive number")
    
