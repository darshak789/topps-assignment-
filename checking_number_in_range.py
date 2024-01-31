#Write a Python function to check whether a number is in a given range.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star} Write a Python function to check whether a number is in a given range.')
print(f'{separator} ' * 35)

def checking_number(number,start,end):
    if number in range(start,end+1):
        print(f'{arrow}  The {number} number is in range.')
    else:
        print(f'{arrow} {number} Number is not in range.')

number=6
start=1
end=10

checking_number(number,start,end)
print(f'{separator} ' * 35)
print(f'{star} Write a Python function to check whether a number is perfect or not.')

import math
def check_abs(num1):
    
input_number=int(input(f'{bullet_point} Enter the number: '))

check_abs(input_number)