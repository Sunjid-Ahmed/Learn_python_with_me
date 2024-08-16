#search for a number x in this tuple using loop [1,4,9,16,25,36,49,64,81,100]
num=(1,4,9,16,25,36,49,64,81,100)
i=0
n=int(input("n:"))
while i < len(num):
    if(num[i]==n):
        print("Found at index",i)
    else:
        print("Finding.....")

    i+=1
