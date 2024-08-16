#multiple inheritence

class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varC="welcome to class C"        

c1=C()

print(c1.varC)
print(c1.varB)
print(c1.varC)