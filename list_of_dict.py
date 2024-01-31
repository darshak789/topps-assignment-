'''Write a Python program to combine values in python list of dictionaries.
Sample data: 
[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})'''
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star} Write a Python program to combine values in python list of dictionaries.')
print(f'{separator} ' * 35)

list_of_dict=[
    {'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, 
    {'item': 'item1', 'amount': 750},{'item': 'item2', 'amount': 750}
    ]
from collections import Counter

combined_counter=Counter()

for entry in list_of_dict:
    item=entry['item']
    amount=entry['amount']
    combined_counter[item]=combined_counter[item] + amount

print(f'{arrow} Expected result is:{combined_counter}')

for items,amount in combined_counter.items():
    print(f'{arrow} {items}:{amount} ',end=' ')
