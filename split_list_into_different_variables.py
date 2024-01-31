star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending='-'*30+'End'+'-'*30

print(f'{star} Write a Python program to split a list into different variables.')
print(f'{separator} ' * 35)

subject_list = [1, 'raj', 8+9j, False, 9.34]

var1, var2, var3, var4, var5 = subject_list

print(f'{bullet_point} Variables assigned are:')
print(f'{arrow} variable1: {var1} with datatype {type(var1)}.')
print(f'{arrow} variable2: {var2} with datatype {type(var2)}.')
print(f'{arrow} variable3: {var3} with datatype {type(var3)}.')
print(f'{arrow} variable4: {var4} with datatype {type(var4)}.')
print(f'{arrow} variable5: {var5} with datatype {type(var5)}.')

print(ending)