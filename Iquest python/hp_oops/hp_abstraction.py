'''
Created on 21-Dec-2025

@author: hp

Abstraction:Data abstraction means showing only the essential features and hiding the complex internal details.

Implemented methods- It has both method name and body 
Un-Implemented methods- It has method name but not method body

Abstract Class: class containing atleast one abstract method 

Interface:class which contains abstract methods only

'''
from abc import abstractmethod, ABC
class HumanBeings(ABC):
    def eating(self):# Implemented method
        print("I am Eating")
        
    @abstractmethod   
    def facial_hair(self):#un-implemented method
        pass# if we define anything we have to add any block of code in next line otherwse error will show so we avoid it we use pass keyword.
        
class Female(HumanBeings):
    def facial_hair(self):
        print("Thin facial hair")
        
#obj1 = HumanBeings()#TypeError: Can't instantiate abstract class HumanBeings with abstract method facial_hair

obj2= Female()
obj2.eating()
obj2.facial_hair()