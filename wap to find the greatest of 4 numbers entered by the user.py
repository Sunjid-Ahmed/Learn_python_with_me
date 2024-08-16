#wap to find the greatest of 4 numbers entered by the user
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=int(input("d:"))
if (a>b and a>c and a>d):
    print("a is the gretest.")
elif(b>a and b>c and b>d):
    print("b is the gretest.")
elif (c>a and c>b and c>d):
    print("c is the gretest.")
else:
    print("d is the gretest.")            