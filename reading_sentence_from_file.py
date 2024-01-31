#Write a Python program to read a random line from a file.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star} Write a Python program to read a random line from a file.')
print(f'{separator} ' * 35)

file=open('test.txt','r')   
print(f'{arrow} Reading file sentence from here:{file.read()}')
file.close()

'''file=open('test.txt','a')
file.write(' this write method would append second line.')
file.close()

file=open('test.txt','r')   
print(file.read())
file.close()

file=open('test.txt','w')
print(file.write('overwritting content.'))
file.close()

file=open('test.txt')
print(file.read())'''