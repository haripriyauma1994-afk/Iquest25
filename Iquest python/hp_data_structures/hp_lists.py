'''
Created on 27-Oct-2025

@author: ABC

List: It is a DS where elements stored within square braces seperadted by commas

1. creation:
    -Empty list can be created
    -List with elements:
        > Manual entry
        > using built-in function - list()/ tuple()/ set()
    -List is heterogeneous: list stores all fundamental data-types including None type

2. Accessing the elements:
   a. - Using index-> list supports indexing.
        Index is a number which represents a position in a DS
        - Positive Index: 
        >Numbering the position from Left-to-right(-->)
        >Index starts with 0,1,2...
        
        - Negative Index
        >Numbering the position from right-to-left (<--)
        >Index starts with -1, -2,-3....
    
     -Syntax: ds_name[index] --> this will return the value present in that index.
     -we get IndexError in following cases
          > Using index greater than or equal to Length of the list.Ex:list4[7]
          > Using index lesser than the nrgative value of the length of the list. Ex:List4[-8]
        

    b.- Using Loops
    c.- Using slicing operator - to access multiple/ group of elements from a DS
    syntax: list_name[start : stop : step]
      -> start - start index (included), default = 0*
      -> stop - stop index (excluded), default = ?
      -> step - increment/ decrement
      
2. Modification: List is mutable(modifiable)
'''
list1 = []
print("list1:", list1)
print(type(list1))

list2 = [2, 5, 6, 8, 4] # Manaully entering elements in the list #homogeneous list
print("list2:", list2)
print(type(list2))

list3 = list(range(6))
print("list3:", list3)
print(type(list3))


#tuple

tuple1 = ()
print("tuple1:", tuple1)
print(type(tuple1))

tuple2 = (2, 5, 6, 8, 4)
print("tuple2:", tuple2)
print(type(tuple2))

tuple3 = (tuple(range(6)))
print("tuple3:", tuple3)
print(type(tuple3))

#set

set1 = {}
print("set1:", set1)
print(type(set1))

set2 = {2, 5, 6, 8, 4}
print("set2:", set2)
print(type(set2))

set3 = set(range(6)) # we cannot use {} symbol in this line bcoz we cannot create set contains another set so remove that.
print("set3:", set3)
print(type(set3))

#list contains elements in different kind of data types #it is called as heteogenous list

list4 = [1,2,3.0,5+6j, True,"hari",None] #list Ds stores all kind of data types
print("list4:", list4)
print(type(list4))

#--- Accessing using Index----

print("list4[3]:", list4[3]) # return the value at 3rd position in list 4, what and all it returned print will collect it and print.
print("list4[-3]:", list4[-3])

#print("list4[3]:", list4[7]) #IndexError:list index out of range
#print("list4[-3]:", list4[-8]) #IndexError: list index out of range

print("Length of list4:", len(list4))

#---- Accessing using Loops----
''' for loop'''

for i in list4:
    print(i)

'''while loop'''

i=0
while i<len(list4): #condition
    print(i)
    #count = count+1 increment
    i+=1 #increment
    
#accessing using while loop
print("============Accessing using while loop=======")
index=0

while index<len(list4):
    print(list4[index])
    index+=1

print("=========slicing operator=======")
print("list4=", list4)
print("list4[0:4]:", list[0:4])
print("list4[::]=", list[::])
print("list[:7:]=", list[:7:])

print("=======Functions specific to Lists=========")
print("list4=", list4)
list4.append(78) #append(object) we can store(add) or passing the value in list.
print("list4=", list4)
list4.append(list2) #append adding at the end of list.
print("list4=", list4)
print("list3=", list3)
list3.clear() #clear()- all the elements in that list removes
print("list3=", list3)
list5 = list4.copy()
print("list5:", list5)
print("id(list4):",id(list4))
print("id(list5):",id(list5))
print(list5.append(67))
print("list4=", list4)
print("list5=", list5)
list5[4]=False
print("list4=", list4)
print("list5=", list5)
print("list5.count(1)",list5.count(1))
print("list5.count(2)",list5.count(2))
list5.extend(list2)
print("list5=", list5)
print("list5.count(2)",list5.count(2))
print("list[8]:", list5[8])
print("list[10]:", list5[10])
#print("list[8][1]:", list[8][1])
print("list5.index(2)):", list5.index(2))
print("list5.index(2,2)):", list5.index(2,2))
#print("list5.index(2,11)):", list5.index(2,11)) ValueError: 2 is not in list

list5.insert(3,100)
print("list5=", list5)#list5= [1, 2, 3.0, 100, (5+6j), False, 'hari', None, 78, [2, 5, 6, 8, 4], 67, 2, 5, 6, 8, 4]

print("list5.pop(5):",list5.pop(5))
print("list5=", list5)

print("list5.remove(78):", list5.remove(78))
print("list5=", list5)

# print("list5.remove():", list5.remove()) # TypeError: list.remove() takes exactly one argument (0 given)
# print("list5=", list5)

list5.reverse()
print("list5=", list5)

list6 = [2, 3, 4, 5, 78, 65, 54, 63, 5, 8, 9]
print("list6:", list6)
list6.sort()
print("list6:", list6)

list6.sort(reverse=True)
print("list6:", list6)
list7=[]
for i in list6:
    if i%2 == 0:
        list7.append(i)
        
print("list7:",list7)

# List Comprehension:

list8 =[j for j in list6 if j%2==0]
print("list8:",list8)


'''
1. Present a list to the user which contains duplicate and unique elements
2. Take any element from the list as input from the user
3. Print how many number of times that element appears in the list
4. Print the indices of that element in the list

'''

list9 = list8 # Aliasing
print("list9:",list9)
print("id(list8):", id(list8))
print("id(list9):", id(list9))
list9[3]=100
print("list8:",list8)
print("list9:",list9)

print("list8 + list5:",list8 + list5) # extending list8 with list5
print("list8*2:", list8*2) # extending the same list twice



