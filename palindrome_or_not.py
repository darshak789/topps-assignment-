#Write a Python function that checks whether a passed string is palindrome or not.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star} Write a Python function that checks whether a passed string is palindrome or not.')
print(f'{separator} ' * 35)

sentence='m adaM' #racecar, nitin

sentence=sentence.lower()
sentence=sentence.replace(" ",'')

rev_sentence=sentence[::-1]

print(f'{bullet_point} Sentence/word is:{sentence}')
if rev_sentence==sentence:
    print(f'{arrow} it is palindrome.')
else:
    print(f'{arrow} it is not palindrome.')