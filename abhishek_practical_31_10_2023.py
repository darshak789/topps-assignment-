star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette = '\u2740'
ending = '-' * 30 + 'End' + '-' * 30

l1=[4,3,6,3,5,32,5,64,2]
l1.sort()
print(l1)
print(f'max number using sort method:{l1[-1]}')

l2=[4,3,6,3,5,32,5,64,2]
print(f'max number using max method:{max(l2)}')

l3=list(range(2,20))

l4=[x for x in l3 if x%2==0]
print('odd number using list comprehension',l4)

odd=0
even=0
for item in l3:
    if item%2==0:
        odd+=1
    else:
        even+=1
    
print(f'odd numbers are {odd} and even numbers are {even}')

t1=(1,2,3,4,5,6,7,8)
print(f'reversed tuple is: ',t1[::-1])

t2=(1,2,3,4,5)
t3=(6,7,8,9,10)
temp=tuple()
temp=t2
t2=t3
t3=t2
print(f' T2 is {t2} and T3 is {t3}')

#c/5= f-32/9
#c=(5(f-32))/9

f=33.8
c= (5 * (f-32) / 9)
print(f'Farenhit to celsius:{f} farenhit to celsius {c}')

alphabet='a'

if alphabet=='a' or alphabet=='e' or alphabet=='i' or alphabet=='o' or alphabet=='u':
    print(f'alphabet is vowel {alphabet}.')
else:
    print(f'alphabet is consonent {alphabet}.')

input_numbers=input('enter the three numbers separated by space:')
numbers_list=input_numbers.split()
print(f'Largest numbers among input is :{max(numbers_list)}')

input_number=int(input('Enter the number:'))

for i in range(1,11):
    print(f'{input_number} * {i} = {input_number*i}')



