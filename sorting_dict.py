#Write a Python script to sort (ascending and descending) a dictionary by value.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star} Write a Python script to sort (ascending and descending) a dictionary by value.')
print(f'{separator} ' * 35)

stud_marks_dict={
    'Ashish':78,
    'Raj':65,
    'Nilesh':9,
    'Rohan':40,
    "Abhishek":54,
    "Shivam":90
}
print(f'{arrow} Orignal dictionary is:\n{stud_marks_dict}')

stud_marks_dict_asc=sorted(stud_marks_dict.items(),key=lambda item:item[1])
print(f'{arrow} In ascending order by values:\n{stud_marks_dict_asc}\n')
stud_marks_dict_desc=sorted(stud_marks_dict.items(),key=lambda item:item[1],reverse=True)
print(f'{arrow} In descending order by values:\n{stud_marks_dict_desc}')
print(white_florette+ending+white_florette)