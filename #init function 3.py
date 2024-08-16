#init function

class student:
    college_name = "ABC college"
    def __init__(self , name , marks):
        self.name = name
        self.marks =marks
        print("Adding new student name in the database....")

s1 = student("karan", 97)
print(s1.name , s1.marks)

s2 = student("gopal", 98)
print(s2.name, s2.marks)
print(s2.college_name)
print(student.college_name) 