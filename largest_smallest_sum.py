'''Write a Python function to get the largest number, smallest num and sum
of all from a list.'''

star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

print(f'''{star} Write a Python function to get the largest number, smallest num and sum
  of all from a list.''')
print(f'{separator} '* 35)
l1=list((1,2,3,4,5,6,7,8,9))
print(l1)
minimum=min(l1)
maximum=max(l1)
summation=sum(l1)
print(f'{arrow} Minimum value:{minimum}')
print(f'{arrow} Maximum value:{maximum}')
print(f'{arrow} Summation is:{summation}')