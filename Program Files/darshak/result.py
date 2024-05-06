name = (input("enter the name:"))
rollno = int(input("enter the roll no:"))
age = int(input("enter the age:"))

m1 = int(input("enter the marks ss:"))
m2 = int(input("enter the marks sk:"))
m3 = int(input("enter the marks guj:"))
totalmarks = m1+m2+m3
print(f"{totalmarks}")
print(totalmarks/3)
if 100 > 90:
    print("a+")
elif 80 < 90:
    print("a")
elif 70 < 80:
    print("b")
elif 60 < 70:
    print("c")
elif 50< 60:
    print("fali")

else:
    print("fali")
