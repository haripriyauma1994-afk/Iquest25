'''
Created on 09-Nov-2025

@author: haripriya

Constructor: Special/magic method used to construct an object with specific features/properties
- Constructor is called implicitly when an object is created
-Constructor can be called explicitly if required
-Constructor can be with parameter or without parameter
-constructor can be defined by a user, if not python will have its own constructor created
'''

class DogClass():
    def __init__(self, name, color, gender, breed):#Constructor #init short form initialisor
        print(f"A dog is created with color:{color}, gender:{gender} and breed:{breed}")
        self.name = name
        self.color = color # selfcolour is a attribute
        self.gender = gender
        self.breed = breed
           
    def bark(self): # method while defining the class it automatically takes self
            print(f"{self.name} is barking")

puppy = DogClass("Tummy","brown", "female", "german sheperd")# puppy is the object 
puppy.bark()
print(type(puppy))

ramana = DogClass("ramana","brown", "male", "German Sheperd")
ramana.bark()
puppy.bark()
print(puppy.name)
print(ramana.name)

print(puppy.color)
print(puppy.gender)
print(puppy.breed)

print(dir(puppy))