'''
Created on 30-Dec-2025

@author: ABC

Random:
'''
import random
import string
from datetime import datetime

print(random.choice([1,4,5,6,7,2,8]))
print(random.randint(0,9))
print(random.choice(string.ascii_lowercase))
print("ss_"+str(datetime.now())+".png")