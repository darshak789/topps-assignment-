#Write a Python program to check whether an element exists within a tuple.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending='-'*30+'End'+'-'*30

print(f'{star} Write a Python program to check whether an element exists within a tuple.')
print(f'{separator} ' * 35)

t1=(1,2,3,4,5)
temp=4

if temp not in t1:
    print(f'{arrow} element is not present.')
else:
    print(f'{arrow} element is present.')

print(f'{bullet_point} Write a Python program to find the length of a tuple.')
print(f'{separator} ' * 35)

print(f'{arrow} Length of tuple is:{(len(t1))}.')

print(f'{bullet_point} Write a Python program to convert a list to a tuple.')
print(f'{separator} ' * 35)

l1=list(t1)
print(f'{arrow} Conversion in list: {l1}.')

print(f'{bullet_point} Write a Python program to reverse a tuple.')
print(f'{separator} ' * 35)

reversed_tuple=t1[::-1]
print(f'{arrow} Reversed tuple: {reversed_tuple}.')

print(f'{bullet_point} Write a Python program to replace last value of tuples in a list.')
print(f'{separator} ' * 35)

t1=[(11,12,13),(14,15,16),(17,18,19)] #13 16 19 should be changed.
new_value='REPLACED'
new_list=[ (item[:-1]+ (new_value,)) for item in t1]
print(f'{arrow} Original tuples in list: {t1}')
print(f'{arrow} Modified tuples in list: {new_list}')



