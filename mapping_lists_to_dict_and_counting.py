#Write a Python program to map two lists into a dictionary.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star} Write a Python program to map two lists into a dictionary.')
print(f'{separator} ' * 35)

keys_=list(map(str,range(1,9)))
values=list(('abhishek'))

dict1=dict(zip(keys_,values))
print(f'{arrow} Mapping:{dict1}.')
print(print(f'{separator} ' * 35))

'''Write a Python program to combine two dictionary adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200,'d':400}
Sample output: Counter
 ({'a': 400, 'b': 400,'d': 400, 'c': 300}).'''

print(f'{bullet_point} Write a Python program to combine two dictionary adding values for common keys.')
d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200,'d':400}
d3=dict()

from collections import Counter
combined_using_keys=Counter(d1) + Counter(d2)
combined_using_keys=dict(combined_using_keys)
print(f'{arrow} Using Counter Class within Collection module:\n{combined_using_keys}.')

dict1=set(d1)
dict2=set(d2)
d3=dict()
for key in dict1|dict2:
    d3[key]=d1.get(key,0)+d2.get(key,0)

print(f'{arrow} using set-operator loop: {d3}')

print(f'{separator} ' * 35)

print(f'{bullet_point} Write a Python program to print all unique values in a dictionary.')

dict1={
    'a':100,
    'b':200,
    'c':100,
    'd':300,
    'e':400,
    'f':200,
    'g':500
}
set1=set(dict1.values())
print(f'{arrow} Unique values by set conversion:\n {set1}')

count_values=Counter(dict1.values())
print(count_values)

unique_list=[value for value,count in count_values.items() if count==1]
print(f'{arrow} Unique values in form of list:\n{unique_list}')
print(ending)