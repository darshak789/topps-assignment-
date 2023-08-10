def sum_three(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum


print(sum_three(20, 1, 2))
print(sum_three(30, 2, 2))
print(sum_three(20, 2, 2))
print(sum_three(1, 20, 3))
