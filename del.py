from decimal import *
import math
input_str='2.45 2.69 2.45 3.45 2.00 0.04 7.25'
input_list=input_str.split()
data = list(map(Decimal, input_list))
print(data)
print("Maximum: ", max(data))
print("Minimum: ", min(data))