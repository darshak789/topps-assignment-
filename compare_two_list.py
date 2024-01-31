star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

print(f'''{star} How will you compare two lists?''')
print(f'{separator} '* 35)

l1=list((range(0,10)))
print(l1)
l2=list((range(11,20)))
print(l2)

if l1==l2: #equality check
    print(f'{arrow} lists are same')
else:
    print(f'{arrow} lists are not same')

#other checks are identity check,containment check,element-wise check.
#https://chat.openai.com/c/f909759e-2d13-4001-8cfa-614c0d966434


