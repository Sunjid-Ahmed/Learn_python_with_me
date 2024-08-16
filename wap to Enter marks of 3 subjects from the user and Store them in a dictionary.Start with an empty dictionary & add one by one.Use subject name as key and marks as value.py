#wap to Enter marks of 3 subjects from the user and Store them in a dictionary.Start with an empty dictionary & add one by one.Use subject name as key and marks as value
dict={

}
print(type(dict))
dict["math"]=input("math:")
dict["chemistry"]=input("chemistry:")
dict["biology"]=input("biology:")
print(dict)

marks={

}
x=int(input("enter phy:"))
marks.update({"phy":x})

x=int(input("enter math:"))
marks.update({"math":x})

x=int(input("enter chem:"))
marks.update({"chem":x})
print(marks)