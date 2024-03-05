#What is used to check whether an object o is an instance of class A?
'''
->The isinstance() function to check whether an object o is an instance of a particular class A.
->The isinstance() function takes two arguments: the object to be checked,
    and the class (or a tuple of classes) against which you want to check the instance.

'''
class A:
    pass

class B:
    pass


obj1=A()
obj2=B()
print(isinstance(obj1,A)) #returns true if if object is instance of class.
print(isinstance(obj2,A))