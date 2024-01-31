'''Write a Python function that takes a list and returns a new list with unique
elements of the first list'''

star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

print(f'''{star} Write a Python function that takes a list and returns a new list with unique
  elements of the first list.''')
print(f'{separator} '* 35)

def unique_values(l1):
    temp=[]
    for x in l1:
        if x not in temp:
            temp.append(x)
        else:
            pass
    
    return temp

input_data=input(f'{bullet_point} Enter the numbers separated by space:')
l1=[int(x) for x in input_data.split()]
result=unique_values(l1)
print(f'{arrow} using loop:{result}')

s1=list(set(l1))

print(f'{arrow} using set method (most efficient algorithm):{s1}')





