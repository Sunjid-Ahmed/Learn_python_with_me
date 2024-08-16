#wap to check if a num is a multiple of 7 or not
num=int(input("num:"))
remainder = num%7 #without this line we can write this  condition in single line
if remainder == 0: #(num%7==0): 
    print("this num is a multiple of 7.")
else:
    print("this num is not a multiple of 7.")    