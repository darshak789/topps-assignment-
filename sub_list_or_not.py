'''Write a Python program to check whether a list contains a sub list'''
star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

print(f'''{star} Write a Python program to count the number of strings where the string
  length is 2 or more and the first and last character are same from a given
  list of strings.''')
print(f'{separator} '* 35)

def check_sub_list(l1,l2):
    s1=set(l1)
    s2=set(l2)
    
    if not s2.difference(s1):   #returns set if sub list is not present: s2-s1
        print(f'{arrow} Sub list is  present.')
    else:
        print(f'{arrow} Sub list is not present.')

main_list=[1,2,3,4,5,6,7,8,9]
sub_list=[5,7,9,9]

check_sub_list(main_list,sub_list)

'''
Using the intersection method to check if a list contains a 
sublist may not be the most efficient approach because it 
compares elements individually and 
may involve creating new sets or lists. 
The time complexity of the intersection method is O(min(len(main_list), len(sub_list))) in the worst case.
In contrast, the Knuth–Morris–Pratt (KMP) algorithm
has a time complexity of O(len(main_list) + len(sub_list)), 
which is generally more efficient, especially for larger lists.'''