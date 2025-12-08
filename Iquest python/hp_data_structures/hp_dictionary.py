'''
Created on 06-Nov-2025

@author: ABC
Dictionary : We store data in the key-value pair within '{}'
Syntax of dictionary 
    {key1:value1,key2:value2,...}

1. Empty Dictionary can be created
2. Dictionary can be created with built-in function dict() using keyword arguements
3. Dictionary doesnt allow duplicate elements
4. When there is duplicate key with different values are present
   last value is assigned to that key
5. When there are elements with different keys but same value are present,
   both the elements are retained/accepted as it is
6. Dictionary can be mutable(modifiable) 


'''

tejas={}
print("dict1 is ",tejas)
print(f"Type of Dictionary is :{type(tejas)}")

print("=======Creation of Dictionary======")

#normal dictionary creation
dict1={1:"Harish",2:"Reshma"}

#create dictionary using built in  functions
dict12=dict(one="Tejas",two="Sai Rohan")
print(dict12)


#dictionary cant be duplicated
dict78={1:"Harish",2:"Reshma",3:"Nimen",3:"Nimen"}
print(dict78)

#dictionary with duplicate keys taking last value
dict67={1:"jai",2:"yogesh",3:"Anu",3:"Rads"}
print(dict67)

#dictionary with duplicate values
dict70={1:"jai",2:"yogesh",3:"Anu",4:"Anu"}
print(dict70)

print("=======Accessing the elements======")
#Accessing with indexing is not ssupported in python
#print(dict70[0]) KeyError: 0

#Accessing the dictionary using keys
print(dict70[3])

#Accessing using for loop for key and values both
for i in dict70:
    print(i,dict70[i])
    
# Accessing by slicing operator is not supported    
#j=dict70[3:4] # Dictionary doesnt support slicing operator 
#print(j)

print("=======Modification of Dictionary======")
#Modification of dictionary 

dict70={1:"jai",2:"yogesh",3:"Anu",4:"Anu"}
dict70[5]="Nitin"
dict70[6]="Great"
dict70[2]="Yogi"

print("Dictionary after modification is below:")
print(dict70)

print("Length of dict70:", len(dict70))

dict71 = dict70.fromkeys(['One', 'Two', 'Three'], 0)

print("dict70",dict70)
print("dict71",dict71)

print(dict70.items())

print(dict70.keys())
print(dict70.values())

for i in dict70.values():
    print(i)

print("=====================")
print(dict70.setdefault(3, "abc"))
print(dict70.setdefault(7, "abc"))
print("dict70:",dict70)

dict70.update(one="Tejas",two="Sai Rohan")
print("dict70:",dict70)

