def test_number5(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False


print(test_number5(71, 62))
print(test_number5(93, 21))
print(test_number5(62, 95))
print(test_number5(37, 259))
print(test_number5(27, 125))
