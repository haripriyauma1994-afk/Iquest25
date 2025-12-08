'''
Created on 23-Oct-2025

@author: Haripriya

"Reduce repetation - increase reuse"--> Easy maintenance

Looping statements:
- Looping statements are used to execute any statement/s repeatedly.
- Any statement/s will be executed repeatedly until a condition is fulfilled

Types of looping statements:
1. While loop: 
   - initial variable -- used to set initial value
   - define the condition
   - increment/ decrement
   
2. For Loop:It is used to iterate(repeating) over a sequence/ range

Loop control statements:
1. break - stop in between
2. continue - skips the execution of statements in a loop available after continue statement once


count= 0 #initial variable

while count<5: #condition
    print("Hello World!")
    #count = count+1 increment
    count+=1 #increment

count= 5 #initial variable

while count>0: #condition
    print("Hello World!")
    #count = count-1 decrement
    count-=1 #decrement

#infinte loops


while True:
    print("Hello World!") #infinite loop

while 1==1:
    print("Hello World!") #infinite loop

#for loop

#print(range(4))

for i in range(1,10,4): #it takes increment
    print(i)     
  

#Break statement

for i in range(1,100): #break statement for For loop
    print(i)
    if i == 50:
        break#it break till user
'''
'''
num=1 #break statement for while loop
while True:#default value
    
    print(num)
    num+=1
    if num==51:#stop the execution we are using if statement is used to break value
        break
#continue statement

for i in range(1,100): #continue statement for For loop
    if i == 50:
        continue #after continue what and all loop is there it will be skiped
    print(i)

 
num=1 #continue statement for while loop
while num<100:
    if num == 50:
        num+=1
        continue
    print(num)
    num+=1
'''
for i in range(1,10,4): #it takes increment
    print(i)     
      
    
    
    
    

