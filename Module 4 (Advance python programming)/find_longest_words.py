#Write a python program to find the longest words.

with open('demo2.txt', 'r', encoding='utf-8') as f: # solving UnicodeDecodeEroor because file contains some incompatible character
    content = f.read()
    words = content.split()
    max_word=max(words,key=len) # below one is in list
    print(max_word)
    
    ''' max_length=max(len(word) for word in words)
   # print(max_length)
    max_word=[word for word in words if max_length==len(word)]
    print(max_word)'''

