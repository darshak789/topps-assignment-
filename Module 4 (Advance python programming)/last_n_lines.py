#Write a Python program to read last n lines of a file
file=open('demo.txt','r')
l1=file.readlines()
print(l1[-1:4:-1])#printing last 3 lines