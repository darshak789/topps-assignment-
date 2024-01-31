#Write a Python program to convert a tuple to a string.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending='-'*30+'End'+'-'*30

print(f'{star} Write a Python program to convert a tuple to a string.')
print(f'{separator} ' * 35)

t1=(1,'RAJ',45.43,False,5+6j,['list'],{'set'},{'key':'value'})

i=1
for item in t1:
    print(f'{arrow} item no {i}: {item} with datatype {type(item)}.')
    i+=1

print(f'{bullet_point} Conversion to string:')

t2=(str(item) for item in t1)
i=1
for item in t2:
    print(f'{arrow} item no {i}: {item} with datatype {type(item)}.')
    i+=1

print(f'{bullet_point} Converting into single string:')

#str1=' '.join(t1) wont print because genrator is exhausted. Need to recreate
#print(f'{arrow} Single string from tuple {str1} with datatype {type(str1)}')

t3=(str(item) for item in t1)
str1=' '.join(t3)
print(f'''{arrow} Single string from tuple: {str1}
    with datatype {type(str1)}''')
print(ending)
