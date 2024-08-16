age=int(input("age:"))
if age >= 18:
    print ("can vote")
    print("can apply for license")
else:
    print ("can not vote")    

#conditional statements

num=int(input("num:"))
if num>2:
    print("is grater than 2")
elif num>3:
    print("is grater than 3")
elif num>4:
    print("is grater than 4")
elif num>5:
    print("is grater than 5")
elif num>6:
    print("is grater than 6")

#grade using conditional statements
                        
marks=input("marks:")
if marks >="90":
    print("A")
elif marks >= "80" and marks < "90":
    print("B")
elif marks >= "70" and marks < "80":
    print("c")
elif marks > "70":
    print("D")                               