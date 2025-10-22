'''
Created on 14-Oct-2025

@author: Haripriya

Operator: It is a symbol which performs operation on one or more operands(variables)

I. classification of operators based on number of operands:
1. Unary operator:acts on single operand Ex: =, -
2. Binary operator:acts on two operands Ex: +, - etc.,
3. Ternary operator: acts on three operands Ex: list comprehension

II. classification of operators based on operations:
 1. Arithmetic operators: addition(+),-,*,/(Quotient),%(Reminder),** (Exponent), //(floor division)
   i/p: numerical
   o/p: numerical
 2. Comparison/Relational Operators: >, <, >=, >=, !=, ==
  i/p: numerical
  o/p:boolean
 3. Assignment Operators: =
 4. Logical Operators: AND, OR, NOT
 AND → Both conditions must be true
 OR → At least one condition must be true
 NOT → Reverses the condition
 i/p: boolean(True/False)
 o/p: boolean
 
 AND(both): If 'a' AND 'b'is true, o/p will be True. Takes 2 i/ps
 OR(anyone): If any of the i/p is true, o/p will be true. Takes 2 i/ps
 NOT(reverse): If i/p is true o/p will be false. Takes 1 i/ps
 
 5. Membership operators: To check whether any element is part of a group
    in, not in
 6. Identity Operators: To check identity / to check whether 2 varibles are identical --is, is not
 7. Unary Minus operator: To negate the numbers
 
 String formatting/ formalizing

'''
print("========Arthmetic Operators========")
a= 20
b = 3
print('a+b: ', a+b)
print('a-b: ', a-b)
print('a*b: ', a*b)
print('a/b: ', a/b)
print('20.0/3: ', 20.0/3)
print('a%b: ', a%b)
print('a**b: ', a**b)
print('a//b: ', a//b)
print('20.0//3: ', 20.0//3)

print("=========Comparison/Relational Operators======")
print("a>b: ",a>b)
print("a<b: ",a<b)
print("a>=b: ",a>=b)
print("a<=b: ",a<=b)
print("a==b: ",a==b)
print("a!=b: ",a!=b)

print("=========Logical Operators=========")
print("=====AND opeartors=======")

print("True and True: ",True and True)
print("True and False: ",True and False)
print("False and True: ",False and True)
print("False and False: ",False and False)

print("=====OR opeartors=======")

print("True or True: ",True or True)
print("True or False: ",True or False)
print("False or True: ",False or True)
print("False or False: ",False or False)

print("=====NOT opeartors=======")

print("not True: ", not True)
print("not False: ", not False)

print("=========Membership Operators=========")
print("'i' in 'vivek'",'i'in 'vivek')
print("'I' in 'vivek'",'I'in 'vivek')
print("'z' in 'vivek'",'z'in 'vivek')
print("'z' not in 'vivek'",'z'not in 'vivek')

print("=========Identity Operators=========")
name1 = 'Vivek'
name2 = 'vivek'
print(id(name1))
print(id(name2))

print("name1 is name2: ", name1 is name2)
print("name1 is not name2: ", name1 is not name2)


#print("'Vivek' is 'Vivek': ", 'Vivek' is 'Vivek'")
#print("'Vivek' is not 'Vivek': ", 'Vivek' is 'Vivek'")



