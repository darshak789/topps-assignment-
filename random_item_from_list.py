star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'

print(f'{star} Write a Python program to select an item randomly from a list.')
print(f'{separator} ' * 35)


def random_number(number_list):
    import random
    if not number_list:
        print(f'{arrow} list is empty')
    else:
        number_list=[int(item) for item in number_list if item.isdigit()]
        if not number_list:
            print(f'{arrow} invalid numbers.')
        else:
            result=random.choice(number_list)
            print(f'{arrow} Random number is {result}.')

input_data=input(f'{bullet_point} Enter the numbers separated by space:') #strings
number_list=input_data.split()
random_number(number_list)



