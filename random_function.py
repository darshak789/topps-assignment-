'''
-How can you pick a random item from a list or tuple?
-How can you pick a random item from a range?
-how can you get a random number in python?
-How will you set the starting value in generating random numbers?
-How will you randomizes the items of a list in place?
'''
separator = '\u25ac'
import random
list1=list(range(1,10))
tup1=tuple(range(10,20))
print(f'from list:{random.choice(list1)}')
print(f'from tuple:{random.choices(tup1,k=2)}')

print(f'{separator} ' * 35)

print(f'from range:{random.randint(20,30)}')

print(f'{separator} ' * 35)

print(f'floating range using uniform: {random.uniform(40.00,50.00)}')

print(f'{separator} ' * 35)

list2=list(range(30,40))
random.shuffle(list2)
print(f'using shuffle:{list2}')

print(f'{separator} ' * 35)

random.seed(12)
print(f'using seed value: {random.randrange(50,60,2)}')
'''
->Setting the same seed value for random number generation provides 
consistent and reproducible results every time you run your program. 
This is because the sequence of random numbers is determined by the seed value.
If you use the same seed, you will get the same sequence of random numbers.

->If we run our program multiple times with this seed,
we will always get the same sequence of random numbers.
This behavior is beneficial for tasks 
where we need consistency and want to reproduce the same random behavior,
such as debugging or testing.'''


