'''
Created on 26-Oct-2025

@author: ABC

* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * * 
* * * * * *

end builtin function: string appended after the last value default a newline or used to define what should be done at the end
what addes to be added to the end of print statement

for j in range(6):#outer loop
    for i in range(6):#inner loop
        print("*", end=" ")
        #print("* * * * * *") #it only works when there is fixed number of "*"(values) in every row
    print() #it is used to print a new line

*
* *
* * * 
* * * *
* * * * *

for i in range(1, 6):          # Loop for rows (1 to 5)
    for j in range(i):         # Loop for stars in each row
        print("*", end=" ")    # Print star and stay on same line
    print()                    # Move to next line after each row
   
   
* * * * * 
* * * * 
* * * 
* * 
*  

for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

#====Square Hollow Pattern======
*  *  *  *  *    
*           *
*           *
*           *
*  *  *  *  *
'''
rows = 5
cols = 5

for r in range(rows):
    for c in range(cols):
        if r == 0 or r == rows-1:
            print("*",end=" ")
    else:
        if c == 0 or c == cols-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    


