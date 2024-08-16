#wap to find the factorial of firt n number (using for loop)
#while loop
n=int (input("n:"))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print ("the factorial is:",fact)

#for loop

n=int (input("n:"))
fact=1
for el in range(1,n+1):
    fact*=el
print ("the factorial is:",fact)
