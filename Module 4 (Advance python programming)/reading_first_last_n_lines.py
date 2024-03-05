#Write a Python program to read first n lines of a file.
#Write a Python program to read last n lines of a file.

with open('demo4.txt','r') as f:
    content=f.readlines()
    print('From beginnig:',content[0:2]) #reading first 2 lines
    print('From last in reverse:',content[-3:][:-1]) #reading last 2 lines and reversing thier order