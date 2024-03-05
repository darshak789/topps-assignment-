    #Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

'''
->Inheritance is acquiring features in a (derived)class from an existing (base) class.
->The main advantage of Inheritance is reusability of code.
->Base Class:'object' In Python, object is the base class for all classes.
    It is the root of the class hierarchy.
    Even if you don't explicitly mention it,
    your class is implicitly a subclass of object.
    ->object provides some basic methods that are inherited by all classes, such as __init__, __str__, __eq__, and others
    ->Implicit Inheritance:
        class MyClass: #If you define a class without explicitly specifying a superclass, it implicitly inherits from object.
        pass
    ->Direct Inheritance:
        class MyClass(object):#You can also explicitly inherit from object:
        pass
    ->Indirect Inheritance:
        class MyBaseClass(object):
        pass
        class MyDerivedClass(MyBaseClass): 
        pass
        #If a class explicitly inherits from another class,
        and that class inherits from object, 
        your class indirectly inherits from object.

->The __init__ method is a special method in Python known as the constructor. 
It is called when an object is created from the class and is used to initialize attributes.

'''

class Animal:
    def __init__(self,name) -> None:
        self.n=name
    
    def speak(self):
        raise NotImplementedError('Subclass should implement this method.') #This method must be override
    
class Dog(Animal):
    def speak(self):
        return f'{self.n}-> Bow Bow!'
    
dog=Dog('Shiro')
print(dog.speak())