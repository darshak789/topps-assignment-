#Write a Python program to count the number of lines in a text file
import pprint
with open('demo3.txt','r') as f:
   
   list_of_lines=f.readlines() #have to remove pprint because pprint shifts cursor to end
   pprint.pprint(list_of_lines)
   f.seek(0)
   print(len(list_of_lines))
   #when counting the number of lines, you should consider the occurrences of newline characters in each string.