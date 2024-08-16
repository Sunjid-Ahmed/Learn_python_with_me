#list method
#append method(add an element at the end of the list)
list1=[2,1,3]
list1.append(4)
print(list1)

#sort the list
list2=[5,7,2,1]
list2.sort()
print(list2)
listab=["banana","litchi","apple"]
listab.sort()
print(listab)

#sort reverse
list2.sort(reverse=True)
print(list2)
listabr=["banana","litchi","apple"]
listabr.sort(reverse=True)
print(listabr)

#reverse list
list3=[3,1,5,7]
list3.reverse()
print(list3)

#insert a new element at index(index,element)
list4=[1,2,3,4,5,6]
list4.insert(2,7)
print(list4)

#remove first occurrence of element(list.remove)

list5=[2,3,5,4,5]
list5.remove(5)
print(list5)
list5.remove(3)
print(list5)

#remove element at index(list.pop)

list6=[1,2,3,4,5,6]
list6.pop(1)
print(list6)

#count 

"""list7=["sunjid","monira",95,98]
list7.count(95)
print(list7)"""

#copy

list7=["sunjid","monira",95,98]
list8=list7.copy()
print("list8:",list8)
