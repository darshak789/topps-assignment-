#Write a Python script to check if a given key already exists in a dictionary.
#Write a Python script to print a dictionary where the keys are numbers between 1 and 15
#Write a Python program to check multiple keys exists in a dictionary.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star} Write a Python script to check if a given key already exists in a dictionary.')
print(f'{separator} ' * 35)

stud_marks_dict={
    'Ashish':78,
    'Raj':65,
    'Nilesh':9,
    'Rohan':40,
    "Abhishek":54,
    "Shivam":90
}

print(f'{bullet_point} Keys of dictionary are: {stud_marks_dict.keys()}.')
print(f'{bullet_point} Checking for Raj key.')

if 'Raj' in stud_marks_dict.keys():
    print(f'{arrow} Key is present.')
else:
    print(f'{arrow} Key isnt present.')

print(f'{separator} ' * 35)

print(f'{bullet_point} Write a Python script to print a dictionary where the keys are numbers between 1 and 15.')

dict1={item:None for item in range(1,16)} #can give item**2
print(f'{arrow} Using dictionary comprehension:\n{dict1}')

print(f'{separator} ' * 35)

print(f'{bullet_point} Write a Python program to check multiple keys exists in a dictionary.')

print(f'{bullet_point} Original dictionary is\n {stud_marks_dict}')

keys_check=['Ashish',"Raj","Ketan"]

for key in keys_check:
    if key in stud_marks_dict.keys():
        print(f'{arrow} {key} is present.')
    else:
        print(f'{arrow} {key} is not present.')
print(ending)
