name= input("enter the name:")
sname= input("enter the sname:")
rollno = int(input("enter the number:"))
age = int(input("enter the age:"))
school= input("enter the school:")

english = int(input("enter the english marks: "))
maths = int(input("enter the marks: "))
science=int(input("enter the marks: "))
hindi=int(input("enter the marks: "))
pysical=int(input("enter the marks: "))
drawing=int(input("enter the marks: "))
sanskit=int(input("enter the marks: "))




totalmarks=(english+maths+science+hindi+pysical+drawing+sanskit)

mark=(totalmarks/7)
print(mark)

if  mark >= 90:
    grade = "A"
elif mark >= 80:
    grade = "B"
elif mark >= 70:
    grade = "C"
elif mark >= 60:
    grade = "D"
elif mark>= 50:
    grade = "F"
elif mark>= 40:
    grade="E"
elif mark>= 30:
    grade="g"
else:
    grade="fail"
print("Grade:", grade)

print("\nMarks Sheet:")

print("\n\n\t\t----------- Mark Sheet -----------\n\n")

print("\t\tschool:",school)
print("\n\t\tfristname:",name,"\t\tlast name:",sname)
print("\n\t\trollno:",rollno)

marks=(round(mark,1))

print(f"""  
---------------------------------------------- Mark Sheet -------------------------------------
|Subject       |\t\t\tMarks\t\t\t|\t\total\t\t|
-----------------------------------------------------------------------------------------------
|English       |\t\t\t{english}\t\t\t|\t\t100\t\t|
|Maths         |\t\t\t{maths}\t\t\t|\t\t100\t\t|
|Science       |\t\t\t{science}\t\t\t|\t\t100\t\t|
|hindi         |\t\t\t{hindi}\t\t\t|\t\t100\t\t|
|pysical       |\t\t\t{pysical}\t\t\t|\t\t100\t\t|
|drawing       |\t\t\t{drawing}\t\t\t|\t\t100\t\t|
|sanskit       |\t\t\t{sanskit}\t\t\t|\t\t100\t\t|
----------------------------------------------------------------------------------------------
|Total Marks   |\t\t\t{totalmarks}\t\t\t|\t\t700\t\t|
|Average Marks |\t\t\t{marks}%\t\t\t|\t\t100\t\t|
|Grade         |\t\t\t{grade}\t\t\t|
----------------------------------------------------------------------------------------------
""")



print(f"Total Marks: ", totalmarks,"\t\tAverage Marks: ",marks,"%")

print("Grade: ", grade)


print(f"""
---------------------------grading system--------------------------
     100-90 | 90-80 | 80-70 | 70-60 | 60-50 |50-40 | 40-30 | 30-0 
        A   |    B  |   C   |     D |    E  |  F   |    F  |  FAIL
     """)

print(f"""
             ---------------                          -----------------                 -----------------
             class reacher                                 principal                          parents
""")