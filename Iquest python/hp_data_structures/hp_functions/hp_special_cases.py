'''
Created on 06-Nov-2025

@author: ABC
4! = 4*3*2*1
   = 4*3!
   = 4*3*2!
   = 4*3*2*1!
   = 4*3*2*1*0!
   = 4*3*2*1*1
0! = 1

4*3!
3*2!
2*1!

1. Recursive function: A function is called within the same function
2. Lambda functions: 
  -we are going to define a function using 'Lambda' keyword instead conventional way
  - Syntax:
      variable_name = lambda arguments : expression

'''
#Recursive function
def factorial(a):
    if a == 0:
        result = 1
    else:
        result = a*factorial(a-1)
    return result
    
print(factorial(4))

#------lambda function-----


add = lambda a,b:a+b
print(add(60,50))

list6=[2,3,4,5,5,8,9,54,63,65,78]
list7=list(filter(lambda a:a%2==0, list6))
print("list7:", list7)

welcome()