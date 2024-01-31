'''Write a Python program to convert a list of characters into a string.'''

star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'

print(f'{star} Write a Python program to convert a list of characters into a string.')
print(f'{separator} ' * 35)

input_data=(input(f'{bullet_point} Enter characters for string conversion:')) #by default in strin type
char_list=input_data.split() #will split it by space and converting into list
char_str=''.join(char_list) #list will be joined together to form a list
print(f'{arrow} String is {char_str}.')




