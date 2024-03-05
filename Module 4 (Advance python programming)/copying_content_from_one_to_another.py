#Write a Python program to copy the contents of a file to another file.

with open('demo4.txt','r') as source:
    content=source.read()

with open('demo5.txt','w') as destination:
    destination.write(content)
    
with open('demo5.txt','r') as f:
    data=f.read()
    print(data)
    