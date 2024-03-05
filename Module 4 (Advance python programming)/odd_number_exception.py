#Write python program that user to enter only odd numbers, else will raise an exception.

num=int(input("Enter the odd number:"))

try:
    if num % 2!=0:
        print("Number is odd")
    else:
        raise ValueError("Exception is raised for even numbers")
        
except ValueError as e:
    print(e)