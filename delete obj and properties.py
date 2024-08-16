class student:
    def __init__(self, name, ):
        self.name = name

s1=student('John')

print(s1.name)  # Output: John
del s1.name  # Delete the object
print(s1.name)  # Output: AttributeError: 'student' object has no attribute
#del s1  # Delete the student object
#print(s1)  # Output: NameError: name 's1' is not defined