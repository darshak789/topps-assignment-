#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.


class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def area(self):
        return f'Area is:{self.l * self.b}'
    
rec=Rectangle(10,10)
print(rec.area())