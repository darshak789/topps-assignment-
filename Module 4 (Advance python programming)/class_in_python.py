#How to Define a Class in Python? What Is Self? Give An Example Of A Python Class.
'''
->object is instance of class.it is behave by properties and attribute of class
->class is template of object. i.e blueprint of object

->self is the instance variable. you can give any name instead of self
     Self is not a keyword  it can be anything. 
     The first we are writing is constructor is  called as (instance variable)
    
    
->if method is accessing instance variable then that method becomes instance method
    In python there are different types of variables and methods:
    Variables: Instance variable  Static variable
    Methods:  Instance method  Class method  Static method

'''

class ClassName:
    class_attribute='Here is class attribute'
    
    def __init__(self,par1,par2) -> None:
        self.par1=par1
        self.par2=par2
        
    def instance_method(self):
        return f'Accessing instance method with {self.par2}'
    
    @classmethod
    def class_method(cls):
        return f'Here is class method with {cls.class_attribute}'
    
    
    @staticmethod
    def static_method():
        return f'Here is static method'
    
obj1=ClassName('Abhishek','Wagh')

print(obj1.instance_method())
print(obj1.class_method()) ## You can call a class method using the class or an instance.
print(ClassName.static_method()) # You can call a static method using the class or an instance.

'''
The @staticmethod and @classmethod decorators in Python 
are used to define static methods and class methods, respectively. 

->The @classmethod decorator is used to define a class method in Python. 
->A class method takes the class itself as its first parameter, commonly named cls. 
->It operates on the class and its attributes, rather than on instances of the class.
->Class methods are bound to the class, not to an instance of the class.

->The @staticmethod decorator is used to define a static method in Python.
A static method is not bound to the instance or the class and does not have access to instance-specific or class-specific data. 
It is a self-contained method that does not modify class or instance state.


Summary:

@classmethod: Used for methods that operate on the class itself and have access to class-level attributes.
@staticmethod: Used for self-contained methods that don't depend on the instance or class state and serve as utility functions within the class's namespace.
'''