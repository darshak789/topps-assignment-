#Write a Python program to create a tuple with numbers.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending='-'*30+'End'+'-'*30

print(f'{star} Write a Python program to create a tuple with numbers.')
print(f'{separator} ' * 35)

start=int(input(f'{ bullet_point} Enter beginning point:'))
end=int(input(f'{ bullet_point} Enter end point:'))
t1=tuple(range(start,end+1))
print(f'{arrow} Tuple with numbers: {t1}')
print(ending)
