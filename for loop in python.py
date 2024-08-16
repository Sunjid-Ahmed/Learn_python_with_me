#for loop in python
list=[1,2,3,4,5,6]
for num in list:
    print(num)

#for loop with else   
for val in list:
    print(val) 
else:
    print("end of loop")  

food=("biriyani","kacchi","pulao","fried rice","noddles")
print(food)
for fav_food in food:
    print(fav_food)   

#str (else )
str="apnacollege"

for char in str:
    if(char =="O"): 
        print("O found")
        break
    print(char)
else:
    print("O not found")    