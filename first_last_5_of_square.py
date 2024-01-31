'''Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.'''
star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

print(f'''{star} Write a Python program to generate and print a list of first and last 5
  elements where the values are square of numbers between 1 and 30.''')
print(f'{separator} '* 35)

l1=[x*x for x in range(1,30) if x<6 or x>24] # 30 is not included
print(f'{arrow} In list mode:{l1}')
numbers=', '.join(map(str,l1))
print(f'{arrow} Numbers:{numbers}')

print(f'{separator} '* 35)

l3=(input(f'{bullet_point} Enter numbers:')) #or you can give int here
l3=[int (x) for x in l3.split()]
l4=[]

for x in l3:
    a=x**2
    l4.append(a)
print(f'{arrow} first 5 elements {l4[0:5:]}') #you can join and map them
print(f'{arrow} last 5 elements {l4[-5::]}')
