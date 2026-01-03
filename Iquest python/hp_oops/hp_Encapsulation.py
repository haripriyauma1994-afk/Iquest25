'''
Created on 21-Dec-2025

Encapsulation: Restricting the access of class elements

capsule - class

Types/ degrees of encapsulation:
1. Public members - No restriction - can be accessed inside class, its sub classes and outside of a class
2. Protected members - can be accessed inside class, its sub classes; prefix: _ (single underscore)
3. Private members - can be accessed inside class only; prefix: __(double underscore)


@author: ABC
'''
class Student:
    school_name = "iQuest" # Static/ class variable
    global day 
    day = "Monday" # Global variable
    
    def __init__(self, name, roll_no, gender):
        self.name = name # Instance/ object variable
        self._roll_no = roll_no
        self.__gender = gender
        # Student.school_name = "iQuest" # # Static/ class variable
        
    def display_details(self):
        print("Student name:", self.name)
        print("Roll No.:", self.roll_no)
        print("School Name:", Student.school_name)
        print("Day", day)
        # Student.school_name = "iQuest" # # Static/ class variable
        
    def calculate_marks(self, kan, eng, maths):
        total_marks = kan+eng+maths # Local variable/ method variable
        self.total_marks = total_marks
        print("Total marks:", total_marks)
        # return total_marks
        
    def display_result(self):
        if self.total_marks>35:
            print("PASS :)")
        else:
            print("FAIL :(")
            

std1 = Student("Vivek", 101, "male")
print(std1.name)
print(std1._roll_no)
# print(std1.__gender)
print(dir(std1))
print(std1._Student__gender)