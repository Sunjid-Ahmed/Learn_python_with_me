#init function

class student:
    college_name = "ABC college"
    name ="anonymous"#class attr
    def __init__(self , name , marks):
        self.name = name  #obj attr>class attr
        self.marks = marks

s1 = student("john", 90)
print(s1.name, s1.marks)   
print(student.name)     
print(s1.name)
print(s1.college_name)
print(student.college_name)