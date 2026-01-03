'''
Created on 30-Dec-2025

@author: ABC
Regular Expressions: Defines the pattern of a string

"ab" --> exact match
"[ab]" --> a or b
"[^ab]" --> except a and b
[a-z] --> any lower case letter
[A-Z] --> any upper case letter
[a-zA-Z] --> any alphabet
[0-9] --> any integer from 0 to 9
[a-zA-Z0-9] --> aplhanumeric character
[^a-zA-Z0-9] --> special character

Quantifiers:

54hvj.h67@iquesttechnologies.co.in
'''
import re

pattern = re.compile("[^ab]")
matcher = pattern.finditer("hgcabjagabajauehab")
# matcher = re.finditer("ab", "hgcabjagabajauehab")
print(matcher)

count=0
for i in matcher:
    # print(i)
    print("Start index:", i.start())
    # print("Stop index:", i.end())
    print("Character:", i.group())
    count+=1
    
print(count)


print(re.search("\AAirtel", "Airtel_Vivek"))

print("====================================")
matcher = re.finditer("a{2,3}", "hgcabajaagaaabajaaaauehab")

count=0
for i in matcher:
    print("Start index:", i.start())
    print("Character:", i.group())

print("====================================")
phone_number_pattern = "\A[6-9]\d{9}$"
print(bool(re.match(phone_number_pattern, "88619110")))

print("=================email validation===================")
email_pattern = "\A[a-zA-Z0-9.-_+]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,}$"
print(bool(re.match(email_pattern, "nvivek.2205@gmail.co.in")))
    