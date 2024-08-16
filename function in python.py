#function
#function definition
def calc_sum(a,b): #a,b are the parameters
    sum=a+b
    print("the sum is:",sum)
    return sum

calc_sum(3,4)  #3,4 are the arguments

calc_sum(5,6) #5,6 are the arguments

calc_sum(7,8) #7,8 are the arguments

calc_sum(9,10) #9,10 are the arguments


#simple function
def cal_sum(a,b): #a,b are the parameters
    return a+b
sum=cal_sum(1,2) #1,2 are the arguments
print("the sum is:",sum)  

#simple function
def print_hello(): #no agrument #no parameter
    print("hello")
print_hello()
print_hello()
print_hello()    

#no parameter #no arguments
def print_hello():
    print("hello")
output=print_hello()
print(output)   

#average of 3 numbers
def avr_3(a,b,c): 
    avr=(a+b+c)/3
    print(avr)
    return avr
avr_3(1,2,3)

#build in function

print("hello","world")

print("hello",end=" ") #sep="" #end="$"
print("world") #end="\n"

#default parameters 
def cal_mul(a=2,b=4):#default parameter should write first #default parameters is only used when there is no arguments
    mul=a*b
    print("the product is:",mul)
    return mul
cal_mul(5,7) #arguments #there we can use singel argument

