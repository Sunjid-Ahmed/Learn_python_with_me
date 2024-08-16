#wap to find the gretest of 3 numbers entered by the user
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if (a>b and a>c):
    print("a is the gretest.")
elif(b>a and b>c):
    print("b is the gretest.")
else:
    print("c is the gretest.")        