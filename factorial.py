#Write a Python function to calculate the factorial of a number (a nonnegative integer).
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star} Write a Python function to calculate the factorial of a number.')
print(f'{separator} ' * 35)

import math
number=5

if number>0:
    fact=math.factorial(number)
    print(f'{arrow} Factorial using math module: {fact}.')
else:
    print(f'{arrow} number is not valid.')