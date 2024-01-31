#Write a Python program to create a tuple with different data types.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending='-'*30+'End'+'-'*30

print(f'{star} Write a Python program to create a tuple with different data types.')
print(f'{separator} ' * 35)

t1=tuple((1,'raj',True,7+8j,23.34,['l1'],{'s1'},{'Teacher': 'Abhi', 'student':'xyz'}))
i=0
for item in t1:
    print(f'{arrow} Item no.{i}: {item} with datatype {type(item)}. ')
    i+=1

print(ending)