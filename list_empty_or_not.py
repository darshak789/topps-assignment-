star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

print(f'''{star} Write a Python program to check a list is empty or not.''')
print(f'{separator} '* 35)

l1=[]

if len(l1)==0:
    print(f'{arrow} List is empty')
else:
    print(f'{arrow} List is not empty')

#you can try other methods too.