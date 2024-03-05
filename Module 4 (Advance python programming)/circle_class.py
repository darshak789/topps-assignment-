#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

import math
class Circle:
    def __init__(self,r) -> None:
        self.r=r
    
    def area(self):
        return math.pi * (self.r**2)
    
    def perimeter(self):
        return 2 * math.pi * self.r
    
    
obj1=Circle(10)
print(f' Area is:{obj1.area():.3f} and\n Perimeter is:{obj1.perimeter():.3f}')