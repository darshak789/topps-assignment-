#Write a Python program to find the repeated items of a tuple.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending='-'*30+'End'+'-'*30

print(f'{star} Write a Python program to find the repeated items of a tuple.')
print(f'{separator} ' * 35)

t1=(1, 2, 2, 3, 4, 4, 5, 5)
repeated_list=[]
l1=list(t1)

for item in l1:
    if t1.count(item) > 1 and item not in repeated_list: #first condition will avoid duplication
        repeated_list.append(item)

t2=tuple(repeated_list)
print(f'{arrow} Original tuple: {t1}.')
print(f'{arrow} Repeated element in form of tuple: {t2}.')
print(f'{ending}')


