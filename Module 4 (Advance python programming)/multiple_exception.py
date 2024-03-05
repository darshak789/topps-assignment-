#Can one block of except statements handle multiple exception?
'''
->In Python, a single except block can handle multiple exceptions.
->You can specify multiple exception types in a single except block,and the block will be executed if any of the specified exceptions occurs. 
->This allows you to group similar exception handling code together,making your code more concise.
->i.e. except (ZeroDivisionError, FileNotFoundError) as e:
'''