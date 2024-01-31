star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

print(f'''{star} Write a Python function that takes two lists and returns true if they have
   at least one common member.''')
print(f'{separator} '* 35)

def common_member_using_loop(l1,l2):
    common_member=[]
    for x in l1:
        if x in l2:
            common_member.append(x)
    
    print(f'{bullet_point} Using intersection method.')
    if common_member:
        common_elements=', '.join(map(str,common_member))
        print(f'{arrow} common members is {common_elements}.')
        #return True no usage here
    else:
        print(f'{arrow} there is no common member')
       # return False

def common_member_using_method(l1,l2):
    s1=set(l1)
    s2=set(l2)

    COMMON_ELEMENTS=s2.intersection(s1)
    Common=', '.join(map(str,COMMON_ELEMENTS))
    print(f'{bullet_point} Using intersection method.')

    if COMMON_ELEMENTS:
        print(f'{arrow} common members is {Common}.')
    else:
        print(f'{arrow} there is no common member')

l1=[1,2,3,4,5,6,7]
l2=[5,6,7,8,9]

common_member_using_loop(l1,l2)
#print('\n')
common_member_using_method(l1,l2)


'''
list1 = [1, 2, 3]
list2 = [1, 4, 3]

s=','.join(map(str,list1))
print(s)
l1=['raj','ab','ad']
p='-'.join(l1)
print(p)

l4=map(str,l1)

for x in l4:
    print(x,end=' ')

'''