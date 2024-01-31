'''Write a Python program to get unique values from a list.'''

star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

print(f'''{star} Write a Python function that takes a list and returns a new list with unique
  elements of the first list.''')
print(f'{separator} '* 35)

input_str=input(f'{bullet_point} Enter numbers separated by space:')
item_list=input_str.split()
item_list=list(set(item_list))
# OR item_list = list(set(map(int, item_list)))
item_list.sort() #lexicographically

result=' '.join(map(str,item_list))
print(f'{arrow} Unique value(s):{result}')
#The map() function is a convenient way 
# to apply a function to every item 
# in an iterable without the need for explicit loops.