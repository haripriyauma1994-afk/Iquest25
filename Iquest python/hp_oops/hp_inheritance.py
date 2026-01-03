'''
Created on 16-Dec-2025

@author: ABC

Inheritance: Is passing of properties(variables/ functions) from one class to another class.
Parent/ Super class: Class from which properties are inherited Ex: GrandFather
Child/ sub class: Class which inherits the properties Ex: Father

Using the object of Child class Parent class properties can be accessed

Types of Inheritance:
1. Single-level inheritance
2. Multi-level inheritance
3. Multiple inheritance

Method Resolution Order: mro()
'''
class GrandFather:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        print(f"Object is created with name:{self.name} and gender: {self.gender}")
        
    def gf_method(self):
        print("This is GrandFather class method")
        
    def home(self):
        print("This is GF's home")
        
class Father(GrandFather):
    
    def __init__(self, name, gender, dob):
        self.dob = dob
        '''
        self.name = name
        self.gender = gender
        print(f"Object is created with dob:{self.dob} name:{self.name} and gender: {self.gender}")
        '''
        
        super().__init__(name, gender)
        print(f"D.O.B.: {self.dob}")
        
    def f_method(self):
        print("This is Father class method")
    
    def home(self):
        print("This is Father's home")
        
class Mother:
    def m_method(self):
        print("This is Mother class method")
        
    def home(self):
        print("This is Mother's home")
        
class Child(Father, Mother):
    def c_method(self):
        print("This is Child class method")
    
    def home(self):
        print("This is Child's home")
        
print("========Grandfather Class==========")
ajja = GrandFather("Gaddappa", "Male")
ajja.gf_method()

print("========Father Class========")
appa = Father("Ayappa", "Male", "01/01/1947")
appa.f_method()
appa.gf_method()

print("=========Child Class=========")
nanu = Child("Maramma","Female", "01/04/2004")
nanu.c_method()
nanu.f_method()
nanu.gf_method()
nanu.m_method()
nanu.home()

'''
print(Child.mro())
print(dir(nanu))
'''
