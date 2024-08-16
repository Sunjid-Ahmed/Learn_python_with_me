#static method

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():
        print("hello")    

s1=student("pk",98)
print(s1.name)
s1.hello()    