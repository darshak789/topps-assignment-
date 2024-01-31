#Write a Python program to find the second smallest number in a list.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'

print(f'{star} Write a Python program to find the second smallest number in a list.')
print(f'{separator} ' * 35)

def smallest_number(item_list):
    valid_numbers=[]
    invalid_numbers=[]

    if item_list:
        for item in item_list:
            if item.isdigit():
                valid_numbers.append(item)
            else:
                invalid_numbers.append(item)
        
        valid_numbers.sort(reverse=True)
        print(f'{arrow} Second smallest number is {valid_numbers[-2]}.')
        if invalid_numbers:
            print(f'{arrow} invalid numbers are {invalid_numbers}.')
        
    else:
        print(f'{arrow} List is empty')


input_data=input(f'{bullet_point} Enter the numbers separated by space:')
item_list=input_data.split()
if len(item_list)>=2:
    smallest_number(item_list)
else:
    print(f'{arrow} Enter two or more numbers.')
