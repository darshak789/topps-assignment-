#Write a Python program to create a dictionary from a string.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star} Write a Python program to create a dictionary from a string.')
print(f'{separator} ' * 35)

str1='madaM'

from collections import Counter
str_to_dict=Counter(str1)
print(f'{arrow } {str_to_dict}')
#str_to_dict_asc=sorted(str_to_dict.items()) # this thing is sorting stringwise as i declared how?
#print(f'{arrow }  sorting keywise: {str_to_dict_asc}')

print(separator)
print(f'{bullet_point} Method 2:Manual Counting.')

letter_count=dict()

str1=str1.lower()
for char in str1:
    if char not in letter_count:
        letter_count[char]=1
    else:
        letter_count[char]+=1
    
print(f'{arrow} Tracking mannually:{letter_count}')