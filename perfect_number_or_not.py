#Write a Python function to check whether a number is perfect or not.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star} Write a Python function to check whether a number is perfect or not.')
print(f'{separator} ' * 35)

input_number=1
def is_perfect_number(num1):
    if num1<=0:
        return False
    divisiors=[x for x in range(1,num1) if num1%x==0]

    if sum(divisiors)==num1:
        return True
    else:
        return False

if is_perfect_number(input_number):
    print(f'{arrow} {input_number} is perfect number.')
else:
    print(f'{arrow} {input_number} is not perfect number.')