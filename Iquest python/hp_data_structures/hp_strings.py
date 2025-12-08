'''
Created on 06-Nov-2025

@author: ABC

'''

String: Group of characters within quotes(double, single, triple-single, triple-double)

Single line strings: single/ double quotes
Multi-line strings: triple-single/ triple-double quotes
'''

# Creation of srings:

empty_string = ""
name = "vivek"
address = """iQuest, #31/B,
            Hebbal Industrial Area,
            Mysuru"""

salary = 100
            
message = 'Welcome to "iQuest"'

action = "eating"

print(f"{name}'s salary is {salary} and works in {address}")

print("{}'s salary is {} and works in {}".format(name, salary, address))

print("{a}'s salary is {b} and works in {c}".format(b=salary, a=name,  c=address))

print(empty_string)
print(type(empty_string))

print(name)
print(type(name))

print(address)
print(type(address))

print(message)
print(type(message))

# Accessing the string elements/ characters in a string:
'''
1. Indexing
2. Slicing
3. Loops
'''

# String modification: String is immutable
print(name)
print(name[2])
# name[2] = 'o' # TypeError: 'str' object does not support item assignment'

# Pre-defined functions specific to strings:
print("========Pre-defined functions specific to strings========")
print(name)
cap_name = name.capitalize()
print("After capitalization:",cap_name)

case_name = address.casefold()
print("After casefold:",case_name)

cent_name = name.center(20, "=")
print("Centralized", cent_name)

print(action.endswith("ing"))

print(name.find("i"))
print(name.isalnum()) # Checks if the string contains alphabet/ numerals
print(address.isalpha())
sentence = '@'.join(["My", "name", "is", "Vivek"])
print(sentence)
ljust_name = name.ljust(20, "=")
print(ljust_name)
rjust_name = name.rjust(20, "=")
print(rjust_name)

print(cent_name.strip("="))
print(sentence.partition("@"))
new_sentence = sentence.replace('@', ' ')
print(sentence)
print(new_sentence)
print(sentence.split('@'))
print(new_sentence.title())