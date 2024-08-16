#search for a number x in this tuple using for loop.[1,4,9,16,25,36,49,64,81,100]
num=[1,4,9,16,25,36,49,64,81,100]
number=int(input("number:"))
for element in num:
    if(element==number):
        print(number,"is found")

        break  
else:
    print(number,"is not found")


#index 
idx=0
for element in num:
    if(element==number):
        print(number,"found at index:",idx)
        #break #(when we want to search for the number once)
        
    idx+=1           