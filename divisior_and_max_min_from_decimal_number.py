#Write a Python program to returns sum of all divisors of a number.
#Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star} Write a Python program to returns sum of all divisors of a number.')
print(f'{separator} ' * 35)

number=8
if number>0:
    divisiors=[x for x in range(1,number+1) if number%x==0]
    print(f'{arrow} sum of divisiors of {number} is {sum(divisiors)}.')
else:
    print(f'{arrow} {number} is not valid. Please enter a positive number.')
print(f'{separator} ' * 35)

print(f'{star} Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.')

input_str='13.5 5.44 8.9 43.4 34.6 95.3 66.3 55.2'
input_list_str=input_str.split()
input_list_decimal=map(float,input_list_str)
list1=[x for x in input_list_decimal]

#float_list=list(map(float,input_list_str.split()))
#float_list=[float(x) for x in input_str.split()]

print(list1)
print(f'{arrow} max number:{max(list1)} and min number:{min(list1)}.')
print(ending)

'''
from decimal import *
data = list(map(Decimal, '2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
print(data)
print("Maximum: ", max(data))
print("Minimum: ", min(data))
-> simplified:
    input_str='2.45 2.69 2.45 3.45 2.00 0.04 7.25'
    input_list=input_str.split()
    data = list(map(Decimal, input_list))'''
