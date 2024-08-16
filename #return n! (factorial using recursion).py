#return n! (factorial using recursion)
x=int(input("x:"))
def fact(n):
    if(n ==1 or n==0):
        return 1
    return fact(n-1) * n

print("the factorial is:",fact(x))