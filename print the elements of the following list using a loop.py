#print the elements of the following list using a loop.[1,4,9,16,25,36,49,64,81,100]
num=[1,4,9,16,25,36,49,64,81,100]

con=len(num) #con means condition
#con=len(num)-1 while idx <= con

#traverse
idx=0
while idx < con:
    print(num[idx])
    idx+=1