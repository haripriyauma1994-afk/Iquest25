'''
 match statement


#create a calulator using match case add,subtract,multiply,divide.

        
while True:   # loop starts

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("choose operation")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")

    operation = input("Enter operation name: ").lower()

    match operation:
        case "add":
            print("Result:", num1 + num2)

        case "subtract":
            print("Result:", num1 - num2)

        case "multiply":
            print("Result:", num1 * num2)

        case "divide":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero!")

        case _:
            print("Invalid operation")

    # asking to continue
    choice = input("Do you want to continue? (yes/no): ").lower()

    if choice != "yes":
        print("done!")
        break   # now break is inside the while loop
'''
#ask user for a day of the week and print if its a weekday or weekend

while True:
        day = int(print("enter the day:")
    match day:
                  
        
        
                
                  
                  
        

    