'''
Created on 21-Oct-2025

'''

# Program to check if a number is positive, negative, or zero
'''
num = float(input('enter the number :'))

if num>0:
    print("The number is positive")
elif num<0:
    print("The number is Negative")
else:
    print("The number is zero")

#Program to find the greatest of three numbers entered by the user

a = int(input("Please enter the first number :"))
b = int(input("please enter the second number:"))
c = int(input("please enter the third number:"))

if a>b and a>c:
    print("greater number is :", a)
elif b>a and b>c:
    print("greater number is :", b)
else:
    print("greater number is :", c)

    
#Accept marks from a student and display the grade based on 

marks=int(input("Enter the marks obtained:"))
if marks>=90:
    print("Grade is : A+")
elif marks>=80 and marks<=89:
    print("Grade is : A")
elif marks>=70 and marks<=79:
    print("Grade is : B")
else:
    print("Grade is: C")
    
#check
print("======even or odd number======")
num2 = int(input("Enter a number:"))
if num2 % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    

#leap year

Year = int(input("please enter a year in yyyy format"))
if Year%100 == 0:
    if Year%400 == 0:
        print(f"{Year} is a leap year")
    else:
        print("This is not a leap year")
    
else:
    if Year%4 == 0:
        print("This is a leap year")
    else:
        print("This is not a leap year")

'''
#Accept an integer and print whether it is divisible by both 3 and 5.

a = int(input("Enter the number"))

if(a%3==0 and a%5==0):
    print("a is divisible by both 3 and 5")
else:
    print("a is not divisible by both 3 and 5")
    
    
    

    



