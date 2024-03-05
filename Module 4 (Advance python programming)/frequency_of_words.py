#Write a Python program to count the frequency of words in a file.

from collections import Counter

with open('demo4.txt','r') as f:
    content=f.read()
    list_data=content.split()
    
    #freq_of_word=Counter((list_data)) # issue of case
    freq_of_word=Counter(map((str.lower),list_data))
    #print(freq_of_word) #will print dictionary
    
    for word,count in freq_of_word.items():
        print(f'{word}->{count}')
    
    