'''Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd'''

star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'''{star} Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.''')
print(f'{separator} ' * 35)

import itertools
dict1={'1':['a','b'],'2':['c','d']}

combinations=list(itertools.product(*dict1.values())) #asterisk is needed otherwise
#(['a', 'b'],)
#(['c', 'd'],)

#for item in combinations:
#    print(item)

l1=[''.join(item) for item in combinations] #['ac', 'ad', 'bc', 'bd']
result=' '.join(l1)
print(f'{arrow} Expected output:{result}')
print(ending)

print(separator)
print(f'{bullet_point} Write a Python program to find the highest 3 values in a dictionary.')

stud_marks_dict={
    'Ashish':78,
    'Raj':65,
    'Nilesh':9,
    'Rohan':40,
    "Abhishek":54,
    "Shivam":90
}
values_list=list(stud_marks_dict.values())
values_list.sort()
print(f'{arrow} Max three values: {values_list[-1:-4:-1]}')
values_list.sort(reverse=True)
max_values=values_list[:3]

keys_3_max=[key for key,value in stud_marks_dict.items() if value in max_values]
print(f'{arrow} keys associated with max 3 values:{keys_3_max}')

for key in keys_3_max:
    value = stud_marks_dict[key]
    print(f' {key}:{value} ',end=' ')
print('\n')
print(ending)

    