#practice class 

class student:
    def __init__(self,name,bangla,english,math):
        self.name=name
        self.bangla=bangla
        self.english=english
        self.math=math


    def average(self):
        return (self.bangla+self.english+self.math) /3

s1=student("karan",98,96,99)
print("The average of three subject:",s1.average())
s1.name="sunjid"
print("The updated name is:",s1.name)        