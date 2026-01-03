'''
Created on 30-Dec-2025

@author: ABC
Exceptions: Errors occurring during runtime

Error:
1. Syntax errors
2. Runtime errors --> exception
    - Logical issues
    - User inputs
    - Server/ memory issues
    
Ways of handling:
1. Permanent fix by altering the logic
2. a. try-except block- default, specific, multiple, nested
   b. try-except-else
   c. try-except-(else)-finally
'''

import traceback
try:
    try:
        num1 = int(input("Please enter an integer:"))
        num2 = int(input("Please enter another integer:"))
        
        print(f"{num1}/{num2}:", num1/num2)
    
    except ZeroDivisionError as ze: # specific exception block
        print(f"{num1}/{num2}", 0/0)
        
except ZeroDivisionError as ze: # specific exception block
        print(f"{num1}/{num2}: Undefined")
        
except (ValueError, TypeError) as vte: # multiple-exception block
    print("Value/Type error:", vte)
    
except Exception as e: # default exception block
    print("Error occured:")
    traceback.print_exception(e)
    
finally: # clean-up actions
    print("Program terminated")