#init function

#default constructors
def __init__(self):
    pass

#parameterized constructor
def __init__(self , name ,marks):
    self.name = name
    self.marks =marks
    print("Adding new student name in the database....")
    

class student:
    college_name = "ABC college"
    def __init__(self , fullname):
        self.name = fullname
        print("Adding new student name in the database....")

s1 = student("karan")
print(s1.name)

s2 = student("gopal")
print(s2.name)
print(s2.college_name)