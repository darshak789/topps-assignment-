#Write a Python program to append text to a file and display the text

file=open('demo.txt','a')
file.write('i am appending data to file')
file.close()

file=open('demo.txt','r')
print(file.read())
file.close()
