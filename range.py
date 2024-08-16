#range
print(range(5))

#print num in range
for el in range(5):#stop
    print(el)

#print num in range(start,stop)

for el in range(1,6):
    print(el)

#print num in range(start,stop,step)

for el in range(1,10,2):
    print(el)   


#print num in range taking from users
n=int(input("n:"))
for el in range(n):
    print(el)