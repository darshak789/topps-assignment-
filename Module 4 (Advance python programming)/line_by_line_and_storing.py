#Write a Python program to read a file line by line and store it into a list
l1=[]
with open('demo.txt','r') as file:
    for line in file:
        l1.append(line)
print(l1)

