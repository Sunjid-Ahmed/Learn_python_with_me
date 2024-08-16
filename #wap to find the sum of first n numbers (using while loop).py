#wap to find the sum of first n numbers (using while loop)
n=int (input("n:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print ("the sum is:",sum)    


n=int (input("n:"))
sum=0
for el in range(1,n+1):
    sum=sum+el
print ("the sum is:",sum)  
    