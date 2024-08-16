#property decorator

class student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        self.percentage=str((self.phy+self.chem+self.maths)/3)+'%'
    
    def calcpercentage(self):
        self.percentage=str((self.phy+self.chem+self.maths)/3)+'%'

stu1=student(80,90,75)
print(stu1.percentage)
stu1.phy=85
print(stu1.phy)
stu1.calcpercentage()
print(stu1.percentage)
