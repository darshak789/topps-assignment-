'''Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.'''

star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

print(f'''{star} Write a Python program to count the number of strings where the string
  length is 2 or more and the first and last character are same from a given
  list of strings.''')
print(f'{separator} '* 35)

input_string=input(f'{bullet_point} Enter the string:')
length_string=len(input_string)
print(f'{arrow} Length of string is {length_string}.')

if len(input_string)>2:
    if input_string[0]==input_string[-1]:
        print(f'{arrow} first and last character is same.')
    else:
        print(f'{arrow} first and last character is not same.')
        
else:
    print(f'{arrow} length is less than or equal to 2')


