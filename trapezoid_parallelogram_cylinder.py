#Write a Python program to calculate the area of a trapezoid.
#Write a Python program to calculate the area of a parallelogram.
#Write a Python program to calculate surface volume and area of a cylinder.

"""
formulas:
-> Area of trapezoid: 1/2 * h *(a+b) where a and b are paralled sides and h is height.
    trapezoid has only one pair parallel.
->Area of parallelogram: b * h where b is base and h is height
    parallelogram has both side parallel.
->Surface area of cylinder: 2 * pi * r * h + 2 * pi * r*r
->Surface volume of cylinder : pi *r *r *h 
"""

star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star} Write a Python program to calculate the area of a trapezoid.')
print(f'{separator} ' * 35)
import math

a=10
b=20
h=30

area_of_trapezoid=0.5 * h * (a+b)
print(f'{arrow} Area of trapezoid is:{area_of_trapezoid}.')
print(f'{separator} ' * 35)

b=5
h=10
area_of_parallelogram= b*h
print(f'{arrow} Area of parallelogram is:{area_of_parallelogram}.')
print(f'{separator} ' * 35)

pi=math.pi

r=10
h=40
surface_area_of_cyl= (2 * pi * (r**2)) + (2 * pi * r * h)
surface_volume_of_cyl=pi * (r**2) * h

print(f'{arrow} Surface area of cyllinder is:{surface_area_of_cyl}.')
print(f'{arrow} Surface volume of cyllinder is:{surface_volume_of_cyl}.')

print(ending)