'''
class Dog:
  name = ''
  color = '' 
  def __init__(self): 
    print("Dog __init__ mathod wad executed") 

print("Py Script file is start running")
classObject = Dog()
print(["classObject", classObject])   
print(["classObject.name", classObject.name])  
'''

class Dog:
  name = ''
  color = ''

  def __init__(self, name_val, color_val):
    self.name = name_val
    self.color = color_val
    print("Dog __init__ mathod wad executed") 

class Cat: 
  def __init__(self, name_val, color_val):
    print("Cat Class Constructors: Special methods used to initialize objects when they are created.") 
    self.name = name_val
    self.color = color_val
    print("Cat __init__ mathod wad executed") 


print("Py Script file is start running")
classObjectDog = Dog("Labrador", "Creamy") 
print(["classObjectDog.name", classObjectDog.name])  
classObjectCat = Cat("RussianCat", "White")   
print(["classObjectCat.name", classObjectCat.name])  