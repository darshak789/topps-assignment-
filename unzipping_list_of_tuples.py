#Write a Python program to unzip a list of tuples into individual lists.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending='-'*30+'End'+'-'*30

print(f'{star} Write a Python program to unzip a list of tuples into individual lists.')
print(f'{separator} ' * 35)

l1=[(1,),(2,3),(4,5,6),(7,8,9),(10,11,12,13)]
max_length=max(len(tup) for tup in l1)

empty_lists=[[] for _ in range(max_length)]
print(empty_lists)

for tup in l1:
    for i,value in enumerate(tup):
        empty_lists[i].append(value)

# Display the individual lists
for i, sublist in enumerate(empty_lists):
    print(f'List {i + 1}: {sublist}')

print(f'{separator} ' * 35)

l1=[(11,12),(13,14),(15,16)]
print(f'{arrow} Original List is: {l1}')

list_of_tuples=list(zip(*l1))
new_list=[list(item) for item in list_of_tuples]

for i,l in enumerate(new_list):
    print(f'{arrow} List{i}: {l}')

print(ending)








