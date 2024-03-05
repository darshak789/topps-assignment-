'''What relationship is appropriate for Course and Faculty?
What relationship is appropriate for Student and Person?'''

'''
Course and Faculty:
-Many-to-Many Association:
    ->If a Course can have multiple Faculty members, and a Faculty member can be associated with multiple Courses, 
        a many-to-many association might be appropriate
    ->If a Course is composed of Faculty members, meaning the existence of a Faculty member is tied to a specific Course, 
        we might consider using aggregation or composition.

Student and Person:
-Inheritance:
    ->if Student is a specific type of Person, we might use inheritance.
'''