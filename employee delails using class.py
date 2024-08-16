#define a employee classwith attributes role ,department and salary ,this class also  a showDetails()method
#create an engineer class that inherits prpperties from employee & has additional attributes:name and age


class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary    

    def showDetails(self):
        print("Role: ", self.role)
        print("Department: ", self.department)
        print("Salary: ", self.salary)  

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 30000)      

eng1=Engineer("John Doe", 30) 
eng1.showDetails()        