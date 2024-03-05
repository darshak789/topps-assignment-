#Write a Python program to read first n lines of a file
file=open('demo.txt','r')
print(file.readlines()) #in one list
print(file.readline()) #only single line will be printed
file.close()
