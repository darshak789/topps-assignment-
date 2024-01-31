#Write a Python program to remove an empty tuple(s) from a list of tuples.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending='-'*30+'End'+'-'*30

print(f'{star} Write a Python program to remove an empty tuple(s) from a list of tuples.')
print(f'{separator} ' * 35)

l1=[1, 2, (3,4), (), (5,6), (), (7,8,9)]

modified_list=[item for item in l1 if item != ()]
#its better to write this 
#modified_list=[ item for item in l1 if item]
print(f'{arrow} Removed empty tuple: {modified_list}')
print(f'{ending}')