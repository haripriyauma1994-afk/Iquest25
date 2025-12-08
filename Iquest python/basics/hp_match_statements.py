'''
Created on 25-Oct-2025

@author: haripriya

matching statement:"Based upon given expression particular case matching the output of given expression.if it doesnot match then default expression as case_."

'''
while True: #repeat the statements continously while loop is required
    
        number = int(input("Please enter day number:"))

        match number:
            case 1:
                print("1 represent Monday")
        
            case 2:
                print("2 represent Tuesday")
    
            case 3:
                print("3 represent Wednesday")
        
            case 4:
                print("4 represent Thursday")
        
            case 5:
                print("5 represent Friday")
        
            case 6:
                print("6 represent Saturday")
    
            case 7:
                print("7 represent Sunday")
        
            case _:
                print("Please enter integer from 1 to 7")
    
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != "yes":# if range is less than 8
            print("Goodbye!")#if no
            break
        