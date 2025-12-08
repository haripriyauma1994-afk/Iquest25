'''
Created on 10-Nov-2025

@author: ABC

Types of variables:
 In python variables are divided into categories as below based on their scope:
 
 1. Local/Method variables:  
        -variables scope is restricted to one particular method
        -Variable value can change from one method to another method 
        -Access:
            within a method with same name
            
 2. Instance/object variables: 
     -scope: object level, but can be used in multiple methods
     but can be used multiple methods
     -change from one method to another method
     Access:
     -within a class-->self.variable_name
     -outside of a class -->obj_name.variable_name
 3. Static/class variables:
     -scope: class level, values remains same for all the objects of that class
     -it will not change
     Access:
     -within a class/Outside of a class
     it can be def in side constructor, outside class, 
4. global variable:
    -declared outside of aclass
    -can be accessed anywherein that module


'''
day="MONDAY" #global variable
class student:
    school_name = "iQuest" #static/class variable
    global day
    day = "Monday" #global variable
    def __init__(self,name,roll_no):
        self.name = name # instance/object variable
        self.roll_no = roll_no
    
        #school_name = "iQuest" static/class variable
        
    def display_details(self):
        print("student name:", self.name)
        print("Roll no:", self.roll_no)
        print("School Name:", student.school_name)
        print("day:")
    def calculate_marks(self, kan, eng, maths):
        total_marks = kan+eng+maths #local variable or method variable
        self.total_marks = total_marks
        print("Total marks:",total_marks)
        #return total_marks
    def display_result(self):
        if self.total_marks>35:
            print("PASS:")
        else:
            print("FAIL:")
            
        