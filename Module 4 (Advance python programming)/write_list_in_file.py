#Write a Python program to write a list to a file.

l1=[1,2,4,'abhishek','Wagh',True]

with open('demo6.txt','a') as f:
    for item in l1:
        f.write( (str(item)+'\n')  )
        
    print('Data appeneded successfully!')