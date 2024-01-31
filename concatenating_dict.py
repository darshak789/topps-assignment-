#Write a Python script to concatenate following dictionaries to create a new one.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star}#Write a Python script to concatenate following dictionaries to create a new one.')
print(f'{separator} ' * 35)

def using_update(dict1,dict2):
    result={}
    result.update(dict1) #result.copy(dict1)
    result.update(dict2)
    
    print(f'{arrow} Concateated dictionary (using update) is:\n{result}')

def using_dict_unpacking(d1,d2):
    result={**d1,**d2}
    print(f'{arrow} Concateated dictionary (using unpacking) is:\n{result}')
    
dict1={'one':1,'two':2,'three':3}
dict2={'four':4,'five':5,'six':6}

print(f'{bullet_point} Original two dictionaries are:\n{dict1} \n {dict2}')

using_update(dict1,dict2)
using_dict_unpacking(dict1,dict2)