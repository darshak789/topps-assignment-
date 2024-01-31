'''Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.'''

star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

print(f'''{star} Write a Python program to remove duplicates from a list.''')
print(f'{separator} '* 35)

def using_set(l1):
    s1=set(l1)
    print(f'{arrow} Using set conversion: {s1} and legth is {len(s1)}.')

def using_loop(l1):
    l2=[]
    for x in l1:
        if x not in l2:
            l2.append(x)
        else:
            pass
    print(f'{arrow} Using loop: {l2} and legth is {len(l2)}.')

l1=['abhishek',True,False,'raj',3,41,5,62,3,5,5.6,'41j','raj']
print(f'{bullet_point} list is {l1} and legth is {len(l1)}.')


using_set(l1)
using_loop(l1)
