#What is Instantiation in terms of OOP terminology?
'''
Instantiation:
->Instantiation is the process of creating an object (instance) of a class.
->It involves allocating memory for the object, 
    initializing its attributes, and returning a reference to the newly created object.
'''

class Car:
    def __init__(self,company,owner) -> None:
        self.c=company
        self.o=owner
        
    def display(self):
        return f'Car company is {self.c} and owner is {self.o}.'

  
obj1=Car("Honda",'Abhishek') # Instantiation

print(obj1.display()) # Accessing object attributes and methods

