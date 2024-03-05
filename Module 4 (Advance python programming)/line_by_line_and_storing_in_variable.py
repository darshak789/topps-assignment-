#Write a Python program to read a file line by line store it into a variable.
variable=''

with open('demo1.txt','r') as file:
    for line in file:  
        variable+=line

print(variable)



    
    

