#practice class 2

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum=0
        for mark in self.marks:
            sum+=mark
        print("hi", self.name ,"your avg score is:" ,sum/3)    

s1=Student("karan",[99,98,97])
s1.average()    
s1.name="sunjid"
s1.average()        