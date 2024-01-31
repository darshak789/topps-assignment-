#Write a Python program to convert a list of tuples into a dictionary.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending='-'*30+'End'+'-'*30

print(f'{star} Write a Python program to convert a list of tuples into a dictionary.')
print(f'{separator} ' * 35)
l1=[('one',2),('two',4),('three',6)]
print(f'{bullet_point} Original List of tuples:{l1}.\n')
d1=dict(l1)
print(f'{arrow} Dictionary:{d1}.\n')

#Write a Python script to sort (ascending and descending) a dictionary by value
print(f'{separator} ' * 35)
#print('\n')

students_marks=[ ("abhi",89),("raj",23),("ashish",80),("shivam",34), ("rohan",65),("nishit",72)]
#lambda input: expression
print(f'{bullet_point} Original Dictionary:\n{students_marks}.\n')
sorted_list_asc=dict(sorted(students_marks,key=lambda item:item[1]))
print(f'{arrow} Sorted dictionary by value in ascending order:\n{sorted_list_asc}.\n')

'''
if there is dictionary
sorted_dict_desc=dict(sorted(students_marks.items(),key=lambda item:item[1],reverse=True))
print(f'{arrow} Sorted dictionary by value in ascending order:\n{sorted_dict_desc}.')'''

sort_list_desc=dict(sorted(students_marks,key=lambda item:item[1],reverse=True))
print(f'{arrow} Sorted dictionary by value in descending order:\n{sort_list_desc}.')
print(ending)